"""Emulator main script."""

from src.config import OPCODES
from src.utils import parse_opcodes


if __name__ == "__main__":
    unprefixed = parse_opcodes(OPCODES["unprefixed"])
    cbprefixed = parse_opcodes(OPCODES["cbprefixed"])

    print(unprefixed[0xFF])