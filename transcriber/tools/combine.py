#!/usr/bin/env python3
import argparse
import glob
import gzip
import json
import logging
import sys

import transcriber.settings as settings


# Wrapper for hiding .gz files
def open_file(filename, mode):
    if filename.endswith(".gz"):
        return gzip.open(filename, mode=mode, compresslevel=settings.compresslevel)
    else:
        return open(filename, mode=mode, buffering=1)


# Initialize logger
def initialize_logger(args):
    if args.log:
        settings.log = getattr(logging, args.log.upper(), None)

        if not isinstance(settings.log, int):
            logging.getLogger("ipal-combine").error(
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

    settings.logger = logging.getLogger("ipal-combine")


def prepare_arg_parser(parser):

    parser.add_argument(
        "files",
        metavar="FILE",
        help="files to combine ('*.gz' compressed).",
        nargs="+",
    )

    parser.add_argument(
        "--dataset",
        dest="dataset",
        metavar="FILE",
        help="original dataset ('*.gz' compressed).",
        required=True,
    )

    parser.add_argument(
        "--output",
        dest="output",
        metavar="FILE",
        help="path to store combined output to ('*.gz' compressed).",
        required=True,
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


def combine(files, dataset, output):

    # Load original dataset
    ds = {}
    settings.logger.info("Loading {} into memory.".format(dataset))

    with open_file(dataset, "rt") as f:
        for line in f.readlines():
            js = json.loads(line)
            js["ids"] = False
            js["metrics"] = {}
            ds[js["timestamp"]] = js

    # Combine datasets
    N = 0

    for file in files:
        N += 1
        settings.logger.info("- Processing file {}/{}: {}".format(N, len(files), file))

        with open_file(file, "rt") as f:
            for line in f.readlines():
                js = json.loads(line)
                assert js["timestamp"] in ds

                ds[js["timestamp"]]["ids"] = ds[js["timestamp"]]["ids"] or js["ids"]
                ds[js["timestamp"]]["metrics"].update(js["metrics"])

    # Save combined dataset
    settings.logger.info("Saving combined dataset")

    with open_file(output, "wt") as f:
        for ts in sorted(ds.keys()):  # ordered by timestamp
            f.write("{}\n".format(json.dumps(ds[ts])))


def main():
    parser = argparse.ArgumentParser()
    prepare_arg_parser(parser)

    args = parser.parse_args()
    initialize_logger(args)

    settings.logger.info(
        "Combining {} files to {}.".format(len(args.files), args.output)
    )

    # Combine
    combine(args.files, args.dataset, args.output)


if __name__ == "__main__":
    main()
