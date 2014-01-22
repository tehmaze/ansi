#pylint: disable=C0103,R0903

from ansi.sequence import sequence
from ansi.colour.base import Graphic
from ansi.colour.fx import bright


black           = Graphic('30')
red             = Graphic('31')
green           = Graphic('32')
yellow          = Graphic('33')
blue            = Graphic('34')
magenta         = Graphic('35')
cyan            = Graphic('36')
white           = Graphic('37')
#gray            = grey                  # US English
default         = Graphic('39')
darkgrey        = bright + black
darkgray        = darkgrey              # US English
brightred       = bright + red
brightgreen     = bright + green
brightyellow    = bright + yellow
brightblue      = bright + blue
brightmagenta   = bright + magenta
brightcyan      = bright + cyan
#white           = bright + grey
