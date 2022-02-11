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
        """Create a new graphics object with a list of commands."""
        self.values = values
        self.sequence = sequence('m', fields=-1)(*values)

    def __add__(self, other: T) -> T:
        """Append either a string to the escape sequence resulting in a new string, or combine with more commands."""
        if isinstance(other, str):
            # For some reason mypy does not understand that T is string in this case
            return cast(T, self.sequence + other)
        elif isinstance(other, Graphic):
            return Graphic(*(self.values + other.values))
        raise NotImplemented('You can only add escape sequences or strings to an escape sequence.')

    def __radd__(self, other: T) -> T:
        """Append either a string to the escape sequence resulting in a new string, or combine with more commands."""
        if isinstance(other, str):
            # For some reason mypy does not understand that T is string in this case
            return cast(T, other + str(self))
        elif isinstance(other, Graphic):
            return Graphic(*(other.values + self.values))
        raise NotImplemented('You can only add escape sequences or strings to an escape sequence.')

    def __call__(self, text: str, reset: bool = True) -> str:
        """Apply the escape sequence to a string, issuing a reset at the end if desired."""
        result = self.sequence + text
        if reset:
            result += str(Graphic('0'))
        return result

    def __str__(self) -> str:
        return self.sequence
