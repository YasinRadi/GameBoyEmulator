from dataclasses import dataclass
from typing import Literal, Optional

@dataclass(frozen=True)
class Operand:

    name: str
    immediate: bool
    bytes: Optional[int] = None
    value: Optional[int] = None
    increment: Optional[bool] = None
    decrement: Optional[bool] = None
    adjust: Optional[Literal["+", "-"]] = None

    def create(self, value):
        return Operand(immediate=self.immediate,
                       name=self.name,
                       bytes=self.bytes,
                       value=value,
                       increment=self.increment,
                       decrement=self.decrement,
                       adjust=self.adjust)
