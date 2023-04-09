"""Emulator main script."""

from pathlib import Path
from disassembler.decoder import Decoder
from md_reader.reader import read_cartridge_metadata


def main():
    """Emulator main function."""
    
    dec = Decoder.create(data=Path('roms/snake.gb').read_bytes(), address=0)
    _, instruction = dec.decode(0x201)

    print(instruction)
    print(instruction.print())

if __name__ == "__main__":
    main()