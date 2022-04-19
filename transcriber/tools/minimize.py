#!/usr/bin/bash
from multiprocessing import Pool
import argparse
import gzip
import json
import logging
import os
import random

import transcriber.settings as settings

WORKER = 4


# Wrapper for hiding .gz files
def open_file(filename, mode):
    if filename.endswith(".gz") or ".gz.tmp-" in filename:
        return gzip.open(filename, mode=mode, compresslevel=settings.compresslevel)
    else:
        return open(filename, mode=mode, buffering=1)


# Initialize logger
def initialize_logger(args):
    if args.log:
        settings.log = getattr(logging, args.log.upper(), None)

        if not isinstance(settings.log, int):
            logging.getLogger("Minimize").error("Option '--log' parameter not found")
            exit(1)

    if args.logfile:
        settings.logfile = args.logfile
        logging.basicConfig(
            filename=settings.logfile, level=settings.log, format=settings.logformat
        )
    else:
        logging.basicConfig(level=settings.log, format=settings.logformat)

    settings.logger = logging.getLogger("Minimize")


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
        help="Number of parallel workers (Default: {}).".format(WORKER),
        default=4,
        required=False,
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


def minimize(input):
    # Generate temprary filename
    tmp = "{}.tmp-{}".format(input, random.randint(1000, 9999))

    # Minimize to temporary file
    with open_file(input, "rt") as fin:
        with open_file(tmp, "wt") as ftmp:
            for line in fin.readlines():

                js = json.loads(line)

                if "state" in js:
                    js["state"] = {}
                if "data" in js:
                    js["data"] = {}

                ftmp.write(json.dumps(js) + "\n")

    # Move temporary file to input
    os.replace(tmp, input)

    print("Minimizing {} done.".format(input))


def main():
    parser = argparse.ArgumentParser()
    prepare_arg_parser(parser)

    args = parser.parse_args()
    initialize_logger(args)

    if args.jobs:
        WORKER = int(args.jobs)

    settings.logger.info(
        "Minimizing {} files with {} jobs.".format(len(args.files), WORKER)
    )

    # Run workers
    with Pool(WORKER) as p:
        p.map(minimize, args.files)


if __name__ == "__main__":
    main()
