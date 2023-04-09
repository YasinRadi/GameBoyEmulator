"""Emulator main script."""

from md_reader.reader import read_cartridge_metadata


def main():
    """Emulator main function."""

    with open("roms/snake.gb", "rb") as rom:
        metadata = read_cartridge_metadata(rom.read())
        print(metadata)

if __name__ == "__main__":
    main()