import sys

from rich import print as rprint


def write_file(*, filename: str, data: str) -> None:
    """Write data to a file"""
    with open(filename, "w") as f:
        f.write(data)


def read_file(*, filename: str) -> str:
    """Read data from a file"""
    with open(filename) as f:
        return f.read()


def confirm_proceed() -> None:
    rprint("Continue: Y/n")
    if "y" not in input().lower():
        sys.exit(0)


def to_yaml(*, data: dict) -> str:
    """Convert a dictionary to YAML"""
    import yaml

    return yaml.dump(data, sort_keys=False)
