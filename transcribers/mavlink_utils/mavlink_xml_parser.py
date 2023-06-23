#!/usr/bin/env python3
import argparse
import gzip
import sys
import xml.etree.ElementTree as ET
from struct import *

from jinja2 import Template

# Converts MAVLink XML definition into Transcriber rules to parse the payload.
# Some default message definitions can be found here:
# https://github.com/mavlink/mavlink/tree/master/message_definitions/v1.0


# Wrapper for hiding .gz files and stdout
def open_file(filename, mode):
    if filename is None:
        return None
    elif filename.endswith(".gz"):
        return gzip.open(filename, mode=mode + "t")
    elif filename == "-":
        return sys.stdout
    else:
        return open(filename, mode=mode, buffering=1)


def render_rules(rules, dest_file):
    # Turn rules into python file rules_mavlink.py using jinja2 templates
    rule_template = """{
            "type": "{{ rule_type }}",
            "var": ["_raw"],
            "method": {{ rule_method }},
            "name": "{{ rule_name }}",
            "remove": False
        },"""
    j2_rule_template = Template(rule_template)

    rules_rendered = {"rules": []}
    for rule in rules:
        rendered = j2_rule_template.render(rule)
        rules_rendered["rules"].append(rendered)

    template = """# These rules have been automatically generated with the mavlinik_xml_parser.py tool!
import struct

JS = {
    "protocols": ["MAVLink"],
    "rules": [
        {% for rule in rules%}{{ rule }}{% endfor %}
    ],
}

"""
    j2_template = Template(template)

    with open_file(dest_file, "w") as mav:
        mav.write(j2_template.render(rules_rendered))


def type_to_hexlen(t):
    # Convert field type to its length in hex (2 hex chars == 1 Byte)
    t = t.split("[")[0] if "[" in t else t
    match t:
        case "int8_t":
            return 1 * 2
        case "uint8_t":
            return 1 * 2
        case "int16_t":
            return 2 * 2
        case "uint16_t":
            return 2 * 2
        case "int32_t":
            return 4 * 2
        case "uint32_t":
            return 4 * 2
        case "int64_t":
            return 8 * 2
        case "uint64_t":
            return 8 * 2
        case "float":
            return 4 * 2
        case "char":
            return 1 * 2
        case "double":
            return 8 * 2
        case _:
            print(f"Unrecognised type: {t}")


def decode_hex(variable, field_type):
    # Generate function to decode variable into specified field type
    # MAVLink sends data in Little Endian, hence struct.unpack('<...)
    # MAVLink2 does not send trailing 0's so padding may be needed, otherwise unpack fails
    types_struct = {
        "char": "c",
        "int8_t": "b",
        "uint8_t": "B",
        "int16_t": "h",
        "uint16_t": "H",
        "int32_t": "i",
        "uint64_t": "Q",
        "int64_t": "q",
        "uint32_t": "I",
        "float": "f",
        "double": "d",
    }

    if field_type == "char":
        # hopefully unsigned chars
        # Decode will fail if the hex is not in the required format
        return f"struct.unpack('<{types_struct[field_type]}', bytes.fromhex({variable}).ljust(struct.calcsize('<{types_struct[field_type]}'), b'\\x00'))[0].decode()"

    return f"struct.unpack('<{types_struct[field_type]}', bytes.fromhex({variable}).ljust(struct.calcsize('<{types_struct[field_type]}'), b'\\x00'))[0]"


def check_if_ordered(fields):
    # Check if fields are ordered by type (technically not nexessary anymore but there for testing)
    if (len(fields)) == 1:
        return True

    for i in range(0, len(fields) - 1):
        if type_to_hexlen(fields[i]["type"]) < type_to_hexlen(fields[i + 1]["type"]):
            return False

    return True


def order_messages(messages):
    # The fields are reordered during transmission WHO THOUGHT THAT WAS A GOOD IDEA?!
    # The XML is already ORDERED !!!!
    # Order fields by type length (arrays dont count)
    for m in messages.values():
        fields = m["fields"]

        if not check_if_ordered(fields):
            ordered_fields = list(fields)

            for i in range(1, len(fields)):  # Insertion Sort
                j = i - 1
                cur = type_to_hexlen(ordered_fields[i]["type"])
                cur_el = ordered_fields[i]

                while j >= 0 and cur > type_to_hexlen(ordered_fields[j]["type"]):
                    ordered_fields[j + 1] = ordered_fields[j]
                    j -= 1

                ordered_fields[j + 1] = cur_el
            m["fields"] = ordered_fields

    return messages


def parse_XML(file):
    tree = ET.parse(file)
    root = tree.getroot()
    messages = {}

    # Assuming just one <messages> element present in XML file
    for message in root.find("messages"):
        # id and name must be present according to spec
        m_id = message.attrib["id"]
        messages[m_id] = {"name": message.attrib["name"], "fields": []}

        # field must be present according to spec
        for field in message.iter("field"):
            messages[m_id]["fields"].append(field.attrib)

    return order_messages(messages)


def parse_into_rules(messages):
    # TODO possible to remove True for last fields
    # TODO possible to re-reorder the message fields according to spec but we'll leave it like this
    # TODO possible to pretty print chars instead of ugly arrays
    rules = []

    for m_id, m in messages.items():
        fields = m["fields"]
        rule_type = m_id
        rule_name = m["name"]
        last_index = 0

        for field in fields:
            rule_name = (
                f"{field['name']}({field['enum']})"
                if "enum" in field
                else field["name"]
            )
            field_type = field["type"]

            if "[" not in field_type:
                field_len = type_to_hexlen(field_type)
                variable = f"x[0][{last_index}:{field_len + last_index}]"
                decoding_method = decode_hex(variable, field_type)
                rule_method = f"lambda x: {decoding_method}"
                last_index += field_len

            else:
                # Type is an array
                var_field_len = type_to_hexlen(
                    field_type.split("[")[0]
                )  # get field type before [X]
                field_len = (
                    int(field_type[field_type.index("[") + 1 : -1]) * var_field_len
                )  # X*type_length
                variable = f"x[0][i+{last_index}:i+{var_field_len + last_index}]"  # to access in hex dump
                decoding_method = decode_hex(variable, field_type.split("[")[0])

                if field_type.split("[")[0] == "char":  # join char array
                    rule_method = f"lambda x: ''.join([{decoding_method} for i in range(0,{field_len},{var_field_len})]).rstrip('\\x00')"
                else:
                    rule_method = f"lambda x: [{decoding_method} for i in range(0,{field_len},{var_field_len})]"

                last_index += field_len

            rule = {
                "rule_type": rule_type,
                "rule_method": rule_method,
                "rule_name": rule_name,
            }
            rules.append(rule)

    return rules


if __name__ == "__main__":
    # Prepare ArgumentParser
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    file = args.file
    output_file = args.output

    # Load XML, parse rules, and generate output
    messages_ordered = parse_XML(file)
    rules = parse_into_rules(messages_ordered)
    render_rules(rules, output_file)
