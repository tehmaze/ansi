#pylint: disable=C0103,R0903

from ansi.colour.base import Graphic


reset           = Graphic('0')
bold            = Graphic('1')
bright          = bold
faint           = Graphic('2')
italic          = Graphic('3')
underline       = Graphic('4')
blink_slow      = Graphic('5')
blink           = Graphic('6')
inverse         = Graphic('7')
conceal         = Graphic('8')
crossed_out     = Graphic('9')
font_reset      = Graphic('10')
normal          = Graphic('22')
blink_off       = Graphic('25')
reveal          = Graphic('28')
