"""Metadata reader."""

import struct
from collections import namedtuple

from .config import FIELDS


CARTRIDGE_HEADER = "".join(format_type for _, format_type in FIELDS)

CartridgeMetadata = namedtuple(
    "CartridgeMetadata",
    [field_name for field_name, _ in FIELDS if field_name is not None],
)

def read_cartridge_metadata(buffer, offset: int = 0x100):
    """
    Unpacks the cartridge metadata from `buffer` at `offset` and
    returns a `CartridgeMetadata` object.
    """
    data = struct.unpack_from(CARTRIDGE_HEADER, buffer, offset=offset)
    return CartridgeMetadata._make(data)
