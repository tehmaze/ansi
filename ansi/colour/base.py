# pylint: disable=C0103,R0903
from typing import Union

from ansi.sequence import sequence

__all__ = ['Graphic']


class Graphic(object):
    '''
    Compose a Select Graphic Rendition (SGR) ANSI escape sequence.
    '''

    def __init__(self, *values: Union[str, "Graphic"]) -> None:
        self.values = values
        self.sequence = sequence('m', fields=-1)(*values)

    def __add__(self, their: Union[str, "Graphic"]) -> Union[str, "Graphic"]:
        if isinstance(their, str):
            return ''.join([str(self), their])
        elif isinstance(their, bytes):  # type: ignore  # This is already checked by the type annotation
            raise TypeError('You can only add strings or strings decorated with escape sequences, not bytes.')
        else:
            return Graphic(*(self.values + their.values))

    def __call__(self, text: str, reset: bool = True) -> str:
        result = self.sequence + text
        if reset:
            result += str(Graphic('0'))
        return result

    def __str__(self) -> str:
        return self.sequence
