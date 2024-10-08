#!/usr/bin/env python3
import argparse
import logging
from pathlib import Path

import orjson

import transcriber.settings as settings
from transcriber.transcriber import open_file

CONFIG_KEYS = [
    "_transcriber-config",
    "_state_extractor-config",
    "_iids-config",
    "_evaluation-config",
]

FORCE_RENAME = False


# Initialize logger
def initialize_logger(args):
    if args.log:
        settings.log = getattr(logging, args.log.upper(), None)

        if not isinstance(settings.log, int):
            logging.getLogger("ipal-join").error("Option '--log' parameter not found")
            exit(1)

    if args.logfile:
        settings.logfile = args.logfile
        logging.basicConfig(
            filename=settings.logfile, level=settings.log, format=settings.logformat
        )
    else:
        logging.basicConfig(level=settings.log, format=settings.logformat)

    settings.logger = logging.getLogger("ipal-join")


def prepare_arg_parser(parser):
    parser.add_argument(
        "files",
        metavar="FILE",
        help="files to join ('*.gz' compressed).",
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
        help="path to store joined output to ('*.gz' compressed).",
        required=True,
    )

    parser.add_argument(
        "--force-rename",
        dest="force_rename",
        help="Forces renaming dict entries, e.g., scores, metrics (Default: False).",
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


def update_dict(orig, add, filename):
    for k, v in add.items():
        if k in orig or FORCE_RENAME:
            k_new = f"{k}-{Path(filename).stem}"
            assert k_new not in orig
            k = k_new

            if not FORCE_RENAME:
                settings.logger.warning(
                    f"key '{k}' already exists! Renaming to '{k_new}'"
                )

        orig[k] = v


def handle_config(ds, js, filename):
    for name in CONFIG_KEYS:
        if name not in js:
            continue

        if name not in ds[js["timestamp"]]:
            ds[js["timestamp"]][name] = {}

        update_dict(ds[js["timestamp"]][name], js[name], filename)


def join(files, dataset, output):
    # Load original dataset
    ds = {}
    settings.logger.info(f"Loading {dataset} into memory.")

    with open_file(dataset, "rt") as f:
        for line in f:
            js = orjson.loads(line)
            js["ids"] = False
            js["scores"] = {}
            js["alerts"] = {}
            ds[js["timestamp"]] = js

    # join datasets
    for N, file in enumerate(files):
        settings.logger.info(f"- Processing {file} ({N + 1}/{len(files)})")

        with open_file(file, "rt") as f:
            for line in f:
                js = orjson.loads(line)
                assert js["timestamp"] in ds

                if "ids" in js:
                    ds[js["timestamp"]]["ids"] = ds[js["timestamp"]]["ids"] or js["ids"]
                if "scores" in js:
                    update_dict(ds[js["timestamp"]]["scores"], js["scores"], file)
                if "alerts" in js:
                    update_dict(ds[js["timestamp"]]["alerts"], js["alerts"], file)

                handle_config(ds, js, file)

    # Save joined dataset
    settings.logger.info("Saving joined dataset")

    with open_file(output, "wb") as f:
        for ts in sorted(ds.keys()):  # ordered by timestamp
            f.write(
                orjson.dumps(
                    ds[ts],
                    option=orjson.OPT_SERIALIZE_NUMPY
                    | orjson.OPT_APPEND_NEWLINE
                    | orjson.OPT_NON_STR_KEYS,
                )
            )


def main():
    global FORCE_RENAME

    parser = argparse.ArgumentParser()
    prepare_arg_parser(parser)

    args = parser.parse_args()
    initialize_logger(args)

    settings.logger.info(f"Combining {len(args.files)} files to {args.output}.")

    FORCE_RENAME = args.force_rename

    # Join
    join(args.files, args.dataset, args.output)


if __name__ == "__main__":
    main()
