"""Emulator main script."""

from disassembler.disassembler import Disassembler


def main():
    """Emulator main function."""
    
    disassembler = Disassembler("roms/snake.gb")
    disassembler.disassemble(0x150, 16)

if __name__ == "__main__":
    main()