"""Decoder class for the disassembler."""


import sys
from dataclasses import dataclass

from config import PREFIXED, INSTRUCTIONS


@dataclass
class Decoder:

    data: bytes
    address: int
    instructions: dict
    prefixed_instructions: dict

    @classmethod
    def create(cls, data: bytes, address: int = 0):
        return cls(
            data=data,
            address=address,
            instructions=INSTRUCTIONS,
            prefixed_instructions=PREFIXED,
        )

    def read(self, address: int, count: int = 1):
        """
        Reads `count` bytes starting from `address`.
        """
        if 0 <= address + count <= len(self.data):
            v = self.data[address : address + count]
            return int.from_bytes(v, sys.byteorder)
        else:
            raise IndexError(f'{address=}+{count=} is out of range')

    def decode(self, address: int):
        """
        Decodes the instruction at `address`.
        """
        opcode = None
        decoded_instruction = None
        opcode = self.read(address)
        address += 1
        # 0xCB is a special prefix instruction. Read from
        # prefixed_instructions instead and increment address.
        if opcode == 0xCB:
            opcode = self.read(address)
            address += 1
            instruction = self.prefixed_instructions[opcode]
        else:
            instruction = self.instructions[opcode]
        new_operands = []
        for operand in instruction.operands:
            if operand.bytes is not None:
                value = self.read(address, operand.bytes)
                address += operand.bytes
                new_operands.append(operand.copy(value))
            else:
                # No bytes; that means it's not a memory address
                new_operands.append(operand)
        decoded_instruction = instruction.copy(operands=new_operands)
        return address, decoded_instruction
    