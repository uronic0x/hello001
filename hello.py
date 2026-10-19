"""Hello World - a minimal demo project."""

import argparse
import sys


def greet(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main() -> int:
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument(
        "-n", "--name",
        default="World",
        help="Name to greet (default: World)",
    )
    args = parser.parse_args()
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
