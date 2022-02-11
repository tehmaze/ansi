import sys

from typing import Any, List, Optional, TYPE_CHECKING, Union

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

if TYPE_CHECKING:
    from ansi.colour.base import Graphic

CSI = '\x1b['
OSC = '\x1b]'
BEL = '\a'


class SequenceGenerator(Protocol):
    def __call__(self, *vals: Union[int, str, "Graphic"]) -> str: ...


def sequence(letter: str, fields: int = 1,
             default: Optional[List[Union[int, str, "Graphic"]]] = None) -> SequenceGenerator:
    """Create a function that creates escape sequences."""

    def _sequence(*values: Union[int, str, "Graphic"]) -> str:
        if len(values) == 0:
            return ''
        output = list(values)
        if fields >= 0 and len(output) > fields:
            raise ValueError('Invalid number of fields, got %d expected %d' %
                             (len(output), fields))

        if default is not None:
            output = output + default[-(fields - len(output)):]

        return ''.join([
            CSI,
            ';'.join(map(str, output)),
            letter,
        ])

    return _sequence


class OSCGenerator(Protocol):
    def __call__(*args: str, **kwargs: Any) -> str: ...


def osc(number: Union[int, str]) -> OSCGenerator:
    """Create a function that creates OSC sequences."""

    def _osc(*args: str, **kwargs: Any) -> str:
        key_value_pairs = ["%s=%s" % (k, v) for (k, v) in kwargs.items()]
        return ''.join([
            OSC,
            str(number),
            ';',
            ';'.join(list(args) + key_value_pairs),
            BEL,
        ])

    return _osc
