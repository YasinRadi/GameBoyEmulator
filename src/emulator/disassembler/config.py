"""Configuration variables."""

import requests

from .utils import parse_opcodes


OPCODES = requests.get("https://gbdev.io/gb-opcodes/Opcodes.json").json()

PREFIXED = parse_opcodes(OPCODES["cbprefixed"])
INSTRUCTIONS = parse_opcodes(OPCODES["unprefixed"])