# GameBoy Emulator

This is a GameBoy emulator written in Python. It allows you to run GameBoy games on your computer using a Python-based emulator.

## Installation

    Clone this repository: git clone https://github.com/YasinRadi/GameBoyEmulator.git
    Install the required dependencies: pip install -r requirements.txt
    Run the emulator: python src/emulator/emulator.py

# Usage

The emulator can be run from the command line using the emulator.py script. You can specify the ROM file you want to run as a command line argument:

python emulator.py game.rom

You can also specify additional options, such as the display size and audio settings, using command line arguments. See the help menu for more information:

```bash
python src/emulator/emulator.py --help
```

# Features

* High level emulation of GameBoy hardware
* Support for most commercial GBA games
* Configurable display and audio settings
* ~~Debugging tools for developers~~
* Save states and rewind functionality
* ~~Support for cheat codes~~

# Contributing

Contributions to this project are welcome! If you find a bug or have a feature request, please open an issue on the GitHub repository. Pull requests are also welcome.

# License

This project is licensed under the MIT License. See the LICENSE.md file for more information.