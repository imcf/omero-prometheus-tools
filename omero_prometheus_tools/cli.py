import argparse

from .chore import serve_metrics


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config", action="append", help="Query configuration files"
    )
    parser.add_argument("-s", "--host", default="localhost")
    parser.add_argument("-u", "--user", default="guest")
    parser.add_argument("-w", "--password", default="guest")
    parser.add_argument(
        "-l", "--listen", type=int, default=9449, help="Serve metrics on this port"
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=60,
        help="Interval (seconds) between updates, default 60",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print verbose output"
    )
    return parser.parse_args()


def main_entry_point():
    args = parse_args()
    serve_metrics(args)
