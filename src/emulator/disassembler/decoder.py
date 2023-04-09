"""Decoder class for the disassembler."""


from pathlib import Path
from dataclasses import dataclass

from config import PREFIXED, INSTRUCTIONS


@dataclass
class Decoder:

    data: bytes
    address: int
    prefixed_instructions: dict
    instructions: dict

    @classmethod
    def create(cls, data: bytes, address: int = 0):
        return cls(
            prefixed_instructions=PREFIXED,
            instructions=INSTRUCTIONS,
            data=data,
            address=address,
        )
