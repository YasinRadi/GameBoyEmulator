"""Main."""

from config import OPCODES
from utils import parse_opcodes


if __name__ == "__main__":
    unprefixed = parse_opcodes(OPCODES["unprefixed"])
    cbprefixed = parse_opcodes(OPCODES["cbprefixed"])

    print(unprefixed[0xFF])