"""Utility functions."""

from .model.operand import Operand
from .model.instruction import Instruction


def parse_opcodes(opcodes: dict) -> dict:    
    return {
        int(hx, base=16): Instruction(
            bytes=op["bytes"],
            cycles=op["cycles"],
            mnemonic=op["mnemonic"],
            opcode=int(hx, base=16),
            operands=[
                Operand(**opr) for opr in op["operands"]
            ],
            immediate=op["immediate"],
        ) for hx, op in opcodes.items()
    }