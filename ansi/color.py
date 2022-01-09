# pylint: disable=C0111,W0611,W0614
from sys import modules

import ansi.colour
from ansi.colour import bg, fg, fx, rgb

modules["ansi.color"] = ansi.colour

__all__ = ['fg', 'bg', 'fx', 'rgb']
