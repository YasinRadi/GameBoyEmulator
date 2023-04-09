"""Instruction file."""
from dataclasses import dataclass

from .operand import Operand


@dataclass
class Instruction:

    bytes: int
    opcode: int
    mnemonic: str
    immediate: bool
    cycles: list[int]
    operands: list[Operand]
    comment: str = ""

    def create(self, operands):
        return Instruction(opcode=self.opcode,
                           immediate=self.immediate,
                           operands=operands,
                           cycles=self.cycles,
                           bytes=self.bytes,
                           mnemonic=self.mnemonic)