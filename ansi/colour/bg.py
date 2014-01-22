#pylint: disable=C0103,R0903

from ansi.colour.base import Graphic
from ansi.colour.fx import bold

# ECMA-048 standard names
black           = Graphic('40')
red             = Graphic('41')
green           = Graphic('42')
yellow          = Graphic('43')
blue            = Graphic('44')
magenta         = Graphic('45')
cyan            = Graphic('46')
white           = Graphic('47')
default         = Graphic('49')

# ECMA-048 bold variants
boldblack       = bold + black
boldred         = bold + red
boldgreen       = bold + green
boldyellow      = bold + yellow
boldblue        = bold + blue
boldmagenta     = bold + magenta
boldcyan        = bold + cyan
boldwhite       = bold + white

# Convenience wrappers
brown           = yellow                # Not in ANSI/ECMA-048 standard
grey            = white                 # Not in ANSI/ECMA-048 standard
gray            = white                 # US English
darkgrey        = boldblack
darkgray        = boldblack             # US English
brightred       = boldred
brightgreen     = boldgreen
brightyellow    = boldyellow
brightbrown     = boldyellow            # Not in ANSI/ECMA-048 standard
brightblue      = boldblue
brightmagenta   = boldmagenta
brightcyan      = boldcyan
brightwhite     = boldwhite
brightgrey      = boldwhite             # Not in ANSI/ECMA-048 standard
brightgray      = boldwhite             # Us English
