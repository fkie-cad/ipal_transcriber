#!/usr/bin/env python3
import argparse
import logging
import os
import random
from itertools import product
from multiprocessing import Pool

import orjson

import transcriber.settings as settings
from transcriber.transcriber import open_file

WORKER = 4

# Keys to keep
RETAIN = [
    "id",
    "timestamp",
    "malicious",
    "ids",
    "scores",
    "alerts",
    "adjust",
    "_transcriber-config",
    "_state_extractor-config",
    "_iids-config",
    "_evaluation-config",
]


# Initialize logger
def initialize_logger(args):
    if args.log:
        settings.log = getattr(logging, args.log.upper(), None)

        if not isinstance(settings.log, int):
            logging.getLogger("ipal-minimize").error(
                "Option '--log' parameter not found"
            )
            exit(1)

    if args.logfile:
        settings.logfile = args.logfile
        logging.basicConfig(
            filename=settings.logfile, level=settings.log, format=settings.logformat
        )
    else:
        logging.basicConfig(level=settings.log, format=settings.logformat)

    settings.logger = logging.getLogger("ipal-minimize")


def prepare_arg_parser(parser):
    parser.add_argument(
        "files",
        metavar="FILE",
        help="files to minimize ('*.gz' compressed).",
        nargs="+",
    )
    parser.add_argument(
        "--jobs",
        dest="jobs",
        metavar="INT",
        help=f"Number of parallel workers (Default: {WORKER}).",
        default=4,
        required=False,
    )
    parser.add_argument(
        "--all",
        dest="all",
        help="Removes all data except those required for evaluation.",
        action="store_true",
    )

    # Logging
    parser.add_argument(
        "--log",
        dest="log",
        metavar="STR",
        help="define logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL). Default is WARNING.",
        required=False,
    )
    parser.add_argument(
        "--logfile",
        dest="logfile",
        metavar="FILE",
        default=False,
        help="File to log to. Default is stderr.",
        required=False,
    )

    # Version number
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {settings.version}"
    )


def minimize(args):
    input, arguments = args
    initialize_logger(arguments)

    # Generate temporary filename
    tmp = f".tmp-{random.randint(1000, 9999)}-{input}"

    # Minimize to temporary file
    with open_file(input, "rt") as fin:
        with open_file(tmp, "wb") as ftmp:
            for line in fin:
                js = orjson.loads(line)

                if "state" in js:
                    js["state"] = {}
                if "data" in js:
                    js["data"] = {}

                if arguments.all:
                    for rm in [key for key in js if key not in RETAIN]:
                        del js[rm]

                ftmp.write(
                    orjson.dumps(
                        js,
                        option=orjson.OPT_SERIALIZE_NUMPY
                        | orjson.OPT_APPEND_NEWLINE
                        | orjson.OPT_NON_STR_KEYS,
                    )
                )

    # Move temporary file to input
    os.replace(tmp, input)

    settings.logger.info(f"Minimizing {input} done.")


def main():
    parser = argparse.ArgumentParser()
    prepare_arg_parser(parser)

    args = parser.parse_args()
    initialize_logger(args)

    # Parse arguments
    WORKER = int(args.jobs)

    settings.logger.info(f"Minimizing {len(args.files)} files with {WORKER} jobs.")

    # Run workers
    with Pool(WORKER) as p:
        p.map(minimize, product(args.files, [args]))


if __name__ == "__main__":
    main()
