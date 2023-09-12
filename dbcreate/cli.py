"""Entry point for the command line interface."""

import sys

from . import db


def run(*args: str) -> None:
# def run(*args: str) -> NoReturn:
    """Runs the command line interface."""
    # if not( \
    combined_args = list(args) + sys.argv[1:]
    # ):
    #     print(f'Usage: {sys.argv[0]} …',
    #           file=sys.stderr)
    #     sys.exit(1)
    print(db.hello(*combined_args[:1]))
    # sys.exit(0)
