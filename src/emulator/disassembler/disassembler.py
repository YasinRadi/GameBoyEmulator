"""Disassembler class."""

from pathlib import Path
from .decoder import Decoder


class Disassembler:
    """Disassembler class.

    This class is responsible for disassembling a binary file into
    a list of instructions.
    """

    def __init__(self, rom_path: str):
        """Initialize a disassembler.

        Args:
            binary_path: The path to the binary file.
        """
        self.decoder = Decoder.create(data=Path(rom_path).read_bytes(), address=0)

    def disassemble(self, address: int, count: int):
        """Disassemble an address.
        
        Args:
            decoder: The decoder to use.
            address: The address to start disassembling from.
            count: The number of bytes to disassemble.
        """
        for _ in range(count):
            try:
                new_address, instruction = self.decoder.decode(address)
                pp = instruction.print()
                print(f'{address:>04X} {pp}')
                address = new_address
            except IndexError as _:
                print('ERROR - {e!s}')
                break
