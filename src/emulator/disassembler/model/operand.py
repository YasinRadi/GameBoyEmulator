from dataclasses import dataclass
from typing import Literal, Optional


def default_if_none(value, condition, else_, negate=False):
    """Returns `value` if `condition` is `None`, else `else_`."""
    cond = condition is not None if negate else condition is None
    return value if cond else else_

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
    
    def print(self):
        adjust = default_if_none(self.adjust, self.adjust, "", negate=True)
        v = (
            default_if_none(self.value, self.bytes, hex(self.value))
            if self.value is not None
            else self.name
        )
        v += adjust
        if self.immediate:
            return v
        return f"({v})"
