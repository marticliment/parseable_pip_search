import argparse
import sys
from urllib.parse import urlencode

from rich.console import Console
from rich.table import Table

from parse_pip_search.parse_pip_search import config, search

from . import __version__
from .utils import check_version


def main():
    ap = argparse.ArgumentParser(
        prog="pip_search", description="Search for packages on PyPI"
    )
    ap.add_argument(
        "-s",
        "--sort",
        type=str,
        const="name",
        nargs="?",
        choices=["name", "version", "released"],
        help="sort results by package name, version or \
                        release date (default: %(const)s)",
    )
    ap.add_argument(
        "query",
        nargs="*",
        type=str,
        help="terms to search pypi.org package repository",
    )
    ap.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    ap.add_argument(
        "--date_format",
        type=str,
        default="%d-%m-%Y",
        nargs="?",
        help="format for release date, (default: %(default)s)",
    )
    args = ap.parse_args()
    query = " ".join(args.query)
    result = search(query, opts=args)
    if not args.query:
        ap.print_help()
        sys.exit(1)
        
    print(" Package | Version | Description ")
    print("---------------------------------")

    for package in result:            
        print(package.name+"|"+package.version+"|"+package.description.replace("\n", ""))


if __name__ == "__main__":
    sys.exit(main())
