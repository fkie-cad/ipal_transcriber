import re

import transcriber.settings as settings


class RuleProcessor:
    def __init__(self, config):
        self.protocols = config.JS["protocols"]
        self.rules = self.__parse_rules(config)
        self.rename = self.__parse_renaming(config)

    def __parse_rules(self, config, fields=["src", "dest", "type"]):

        self.fields = fields

        if "rules" not in config.JS:
            settings.logger.info("No attribute 'rules' found in config file")
            return []

        rules = []
        for rule in config.JS["rules"]:

            # Check rule integrity
            if "var" not in rule or not isinstance(rule["var"], list):
                # 'var' : [...] required
                settings.logger.warning(
                    "No attribute 'var' in rule or not of type list!"
                )
                settings.logger.warning("Ignoring rule: {}".format(rule))
                continue

            if bool("name" in rule) != bool("method" in rule):
                # method <-> name
                settings.logger.warning("Set method and name or none of both!")
                settings.logger.warning("Ignoring rule: {}".format(rule))
                continue

            # Compile regex for filtering messages or default to True
            for field in fields:
                if field in rule:
                    rule[field] = re.compile(rule[field]).fullmatch
                else:
                    rule[field] = lambda x: True

            rules.append(rule)

        return rules

    def __parse_renaming(self, config):

        if "rename" not in config.JS:
            settings.logger.info("No attribute 'rename' found in config file")
            return []

        rules = []
        for match, new_name in config.JS["rename"].items():
            rules.append([re.compile(match).fullmatch, new_name])

        return rules

    def __matches(self, msg, rule):

        # Apply regex to each field to check (fields)
        matches = [
            rule[field](str(getattr(msg, field))) is not None for field in self.fields
        ]
        return all(matches)

    def apply(self, msg):

        if msg.protocol not in self.protocols:
            return

        for rule in self.rules:

            # Does rule match
            if not self.__matches(msg, rule):
                continue

            # Call rule method
            if "method" in rule:
                try:  # Try extract vars
                    vars = [msg.data[var] for var in rule["var"]]
                    msg.data[rule["name"]] = rule["method"](vars)
                except KeyError:
                    settings.logger.debug(
                        "Rules: Key {} not found in msg".format(rule["var"])
                    )

            # Remove old entries
            if "remove" in rule and rule["remove"]:
                for var in rule["var"]:
                    try:
                        del msg.data[var]
                    except KeyError:
                        settings.logger.debug(
                            "Rules: Key {} not found during removing".format(var)
                        )

        # Rename src or dest
        for matches, new_name in self.rename:
            if matches(msg.src):
                msg.src = new_name
            if matches(msg.dest):
                msg.dest = new_name
