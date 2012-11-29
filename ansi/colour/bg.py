#pylint: disable=C0103,R0903

from ansi.sequence import sequence
from ansi.colour.base import Graphic
from ansi.colour.fx import bright

black           = Graphic('40')
red             = Graphic('41')
green           = Graphic('42')
brown           = Graphic('43')
blue            = Graphic('44')
magenta         = Graphic('45')
cyan            = Graphic('46')
grey            = Graphic('47')
gray            = grey                  # US English
default         = Graphic('49')
darkgrey        = bright + black
darkgray        = darkgrey              # US English
brightred       = bright + red
brightgreen     = bright + green
yellow          = bright + brown
brightblue      = bright + blue
brightmagenta   = bright + magenta
brightcyan      = bright + cyan
white           = bright + grey
