"""Configuration variables."""

import json


with open("opcodes.json", "r") as f:
    OPCODES = json.load(f)