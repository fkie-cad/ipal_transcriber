import json
import math
import re
from pathlib import Path
from subprocess import PIPE, Popen
from typing import List, Optional, Tuple, Union

# Exclude output paths
collect_ignore = ["snapshots"]

WORKING_DIRECTORY = Path(__file__).parent.parent
TRANSCRIBER = WORKING_DIRECTORY / "ipal-transcriber"
STATE_EXTRACTOR = WORKING_DIRECTORY / "ipal-state-extractor"


########################
# Helper methods
########################


def run_command(
    command: Union[str, Path],
    args: List[str],
    cwd: Optional[Union[str, Path]] = None,
    stdin: Optional[bytes] = None,
) -> Tuple[int, bytes, bytes]:
    """
    Runs a command with the provided arguments and optional stdin input.

    :param command: The command to run.
    :param args: List of arguments to pass to the command.
    :param cwd: Optional working directory. Defaults to two levels up from this script if not provided.
    :param stdin: Optional bytes input to pass to the command's stdin.
    :return: A tuple containing the return code, stdout, and stderr.
    """
    # Resolve the default cwd as two levels up from the current file's directory
    if cwd is None:
        cwd = WORKING_DIRECTORY
    # Convert command and cwd to string paths if they are Path objects
    command = str(command)
    cwd = str(cwd)

    # Execute the command with optional stdin
    p = Popen(
        [command] + args,
        stdout=PIPE,
        stderr=PIPE,
        stdin=PIPE if stdin else None,
        cwd=cwd,
    )
    stdout, stderr = p.communicate(input=stdin)
    return p.returncode, stdout, stderr


def transcriber(args: List[str]) -> Tuple[int, bytes, bytes]:
    return run_command(TRANSCRIBER, args)


def extractor(args: List[str]) -> Tuple[int, bytes, bytes]:
    return run_command(STATE_EXTRACTOR, args)


def check_command_output(
    returncode: int,
    args: List[str],
    stdout: bytes,
    stderr: bytes,
    expectedcode: int = 0,
    expected_stderr: List[Union[bytes, str]] | None = None,
    expected_stdout: List[Union[bytes, str]] | None = None,
    check_for: List[str] | None = None,
):
    """
    Checks returncode and, if given, stderr and stdout, printing debug information if needed.

    :param returncode: Code to check.
    :param args: List of command arguments ran.
    :param stdout: The command's stdout.
    :param stderr: The command's stderr.
    :param expectedcode: Expected return code, default is 0.
    :param expected_stderr: Expected stderr, given as a list of bytes and/or regex strings, default is to not check.
    :param expected_stdout: Expected stdout, given as a list of bytes and/or regex strings, default is to not check.
    :param check_for: Checks stderr for certain strings, used to check for "ERROR" or "WARNING"
    """

    if check_for:
        for phrase in check_for:
            if phrase.encode() in stderr:
                print_command_failure(
                    returncode,
                    expectedcode,
                    args,
                    stdout,
                    stderr,
                    "stderr",
                    expected_stderr,
                )
                assert False, f'"{phrase}" found in stderr when it was not expected'

    if expected_stderr and not match_output(stderr, expected_stderr):
        print_command_failure(
            returncode, expectedcode, args, stdout, stderr, "stderr", expected_stderr
        )
        assert False, "stderr did not match any expected patterns or bytes"

    if expected_stdout and not match_output(stdout, expected_stdout):
        print_command_failure(
            returncode, expectedcode, args, stdout, stderr, "stdout", expected_stdout
        )
        assert False, "stdout did not match any expected patterns or bytes"

    if returncode != expectedcode:
        print_command_failure(
            returncode, expectedcode, args, stdout, stderr, "returncode"
        )
        assert returncode == expectedcode


def print_command_failure(
    returncode: int,
    expectedcode: int,
    args: List[str],
    stdout: bytes,
    stderr: bytes,
    stream_type: str,
    expected: List[Union[bytes, str]] | None = None,
):
    """
    Print detailed information when a command fails.

    :param returncode: The actual return code.
    :param expectedcode: The expected return code.
    :param args: List of command arguments.
    :param stdout: The command's stdout.
    :param stderr: The command's stderr.
    :param stream_type: Type of stream ("stderr", "stdout", or "returncode") that caused the failure.
    :param expected: The expected patterns or bytes for the failing stream (stdout or stderr).
    """
    print(f"{'=' * 20} COMMAND FAILED {'=' * 20}")

    if stream_type == "returncode":
        print(f"Unexpected returncode: {returncode}, expected {expectedcode}")
    else:
        print(f"Unexpected {stream_type}.")
        if expected:
            print(f"Expected one of the following {stream_type}:")
            for exp in expected:
                print(f"  - {repr(exp)}")

    print(f"Command args: {' '.join(args)}")
    print("-- STDOUT --")
    print(stdout.decode("utf-8"))
    print("-- STDERR --")
    print(stderr.decode("utf-8"))


def match_output(output: bytes, expected: List[Union[bytes, str]]) -> bool:
    """
    Check if the output matches any of the expected patterns or bytes.

    :param output: The actual output to check.
    :param expected: List of expected patterns or bytes.
    :return: True if a match is found, otherwise False.
    """
    for exp in expected:
        if isinstance(exp, bytes) and output == exp:
            return True
        elif isinstance(exp, str) and re.search(exp, output.decode("utf-8")):
            return True
    return False


def normalize(content):
    normalized = ""
    for line in content.splitlines():
        normalized += f"{json.dumps(json.loads(line), indent=4, ensure_ascii=False, sort_keys=True)}\n"
    return normalized


def calculate_and_create_paths(filename: str, prefix: str):
    if prefix:
        prefix += "_"
    base_path = Path(__file__).parent / "snapshots"
    output_path = base_path / "output" / f"{prefix}{filename}"
    tmp_path = base_path / "tmp" / f"{prefix}{filename}"
    validation_path = base_path / "validation" / f"{prefix}{filename}"
    output_path.parent.mkdir(exist_ok=True)
    tmp_path.parent.mkdir(exist_ok=True)
    validation_path.parent.mkdir(exist_ok=True)
    return output_path, tmp_path, validation_path


def assert_file_contents_equal(
    validation_path: Path, output_path: Path, tolerance: float = 1e-15
):
    """
    Compares test output with validation files, compares json recursively with tolerance for float values.
    :param validation_path: validation path
    :param output_path: content file to be checked
    :param tolerance: float tolerance used during comparison
    :return:
    """

    with validation_path.open("r") as val_file, output_path.open("r") as out_file:
        validation_lines = val_file.readlines()
        output_lines = out_file.readlines()

        if len(validation_lines) != len(output_lines):
            print(f"{'=' * 25} Start of error {'=' * 25}")
            print("Output lengths don't match, test failed!")
            print("Validation file content:")
            print("\n".join(validation_lines))
            print("\nOutput file content:")
            print("\n".join(output_lines))
            print(f"{'=' * 25}End of error{'=' * 25}")
            assert False, (
                f"Line count mismatch: {len(validation_lines)} lines in validation file "
                f"vs {len(output_lines)} lines in output file."
            )

        # Filter out lines with the ignore marker
        validation_lines, output_lines = filter_ignore_lines(
            validation_lines, output_lines
        )

        try:
            # Parse the filtered content as JSON
            validation_data = json.loads("".join(validation_lines))
            output_data = json.loads("".join(output_lines))

            compare_json_with_tolerance(validation_data, output_data, tolerance)
        except json.JSONDecodeError:
            # if it's not a json file but line by line json, try this:
            try:
                for validation_line, output_line in zip(validation_lines, output_lines):
                    validation_data_line = json.loads(validation_line)
                    output_data_line = json.loads(output_line)

                    compare_json_with_tolerance(
                        validation_data_line, output_data_line, tolerance
                    )
            except json.JSONDecodeError:
                # If not JSON, fallback to direct text comparison
                for i, (val, out) in enumerate(zip(validation_lines, output_lines)):
                    if "###IGNORE-LINE###" not in val and val != out:
                        print(f"{'=' * 25} Start of error {'=' * 25}")
                        print("Output line didn't match, test failed!")
                        print(f"Validation file content (Line {i + 1}): {val}")
                        print(f"Output file content (Line {i + 1}): {out}")
                        print(f"{'=' * 26} End of error {'=' * 26}")
                        assert False, (
                            f"Line {i + 1} mismatch:\n"
                            f"Validation: {val}\n"
                            f"Output: {out}"
                        )


def compare_json_with_tolerance(expected, actual, tolerance: float):
    """
    Recursively compare two JSON objects with a specified tolerance for float comparisons.
    """
    if isinstance(expected, dict) and isinstance(actual, dict):
        for key in expected:
            assert key in actual, f"Key '{key}' not found in actual JSON."
            compare_json_with_tolerance(expected[key], actual[key], tolerance)
    elif isinstance(expected, list) and isinstance(actual, list):
        assert len(expected) == len(
            actual
        ), f"List lengths differ: {len(expected)} != {len(actual)}"
        for expected_item, actual_item in zip(expected, actual):
            compare_json_with_tolerance(expected_item, actual_item, tolerance)
    elif isinstance(expected, float) and isinstance(actual, float):
        if math.isnan(expected) and math.isnan(actual):
            pass  # Both are NaN, considered equal
        else:
            assert (
                abs(expected - actual) <= tolerance
            ), f"Value mismatch: {expected} != {actual} within tolerance {tolerance}"
    else:
        assert expected == actual, f"Value mismatch: {expected} != {actual}"


def filter_ignore_lines(
    validation_lines: List[str], output_lines: List[str]
) -> Tuple[List[str], List[str]]:
    """
    Filter out lines containing '###IGNORE-LINE###' from both validation and output lines.

    :param validation_lines: List of lines from the validation file.
    :param output_lines: List of lines from the output file.
    :return: A tuple containing the filtered validation and output lines.
    """
    filtered_validation_lines = []
    filtered_output_lines = []

    for v_line, o_line in zip(validation_lines, output_lines):
        if "###IGNORE-LINE###" not in v_line:
            filtered_validation_lines.append(v_line)
            filtered_output_lines.append(o_line)

    return filtered_validation_lines, filtered_output_lines


def check_with_validation_file(
    filename: str, raw_content: str, prefix: str = "", tolerance: float = 1e-15
):
    """
    Compares test output with validation file, compares json recursively with tolerance for float values.
    :param filename: validation file name
    :param raw_content: content to be checked
    :param prefix: test prefix for validation file
    :param tolerance: float tolerance used during comparison
    :return:
    """
    print(f"Processing validation file: {filename}")
    print(f"Content length: {len(raw_content)} characters")
    print(f"Prefix used: '{prefix}'")

    output_path, tmp_path, validation_path = calculate_and_create_paths(
        filename, prefix
    )

    normalized_content = normalize(raw_content)

    tmp_path.write_text(raw_content)
    output_path.write_text(normalized_content)
    assert validation_path.is_file(), (
        f"Validation file for '{filename}' does not exist. "
        f"Test output can be found under: {output_path}"
    )

    assert_file_contents_equal(validation_path, output_path, tolerance=tolerance)
