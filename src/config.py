"""Configuration variables."""

import requests


OPCODES = requests.get("https://gbdev.io/gb-opcodes/Opcodes.json").json()