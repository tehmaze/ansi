# pylint: disable=C0103,R0903
from typing import TypeVar, Union, cast

from ansi.sequence import sequence

__all__ = ['Graphic']

T = TypeVar('T', str, 'Graphic')


class Graphic(object):
    '''
    Compose a Select Graphic Rendition (SGR) ANSI escape sequence.
    '''

    def __init__(self, *values: Union[str, "Graphic"]) -> None:
        self.values = values
        self.sequence = sequence('m', fields=-1)(*values)

    def __add__(self, their: T) -> T:
        if isinstance(their, str):
            # For some reason mypy does not understand that T is string in this case
            return cast(T, self.sequence + their)
        elif isinstance(their, Graphic):
            return Graphic(*(self.values + their.values))
        raise TypeError('You can only add strings or strings decorated with escape sequences together.')

    def __call__(self, text: str, reset: bool = True) -> str:
        result = self.sequence + text
        if reset:
            result += str(Graphic('0'))
        return result

    def __str__(self) -> str:
        return self.sequence
