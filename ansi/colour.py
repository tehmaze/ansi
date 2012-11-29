#pylint: disable=C0103,R0903

from ansi.sequence import sequence


__all__ = ['reset', 'bold', 'bright', 'faint', 'italic', 'underline',
    'inverse', 'conceal', 'crossed_out', 'font_reset', 'normal', 'blink_off',
    'reveal', 'Foreground', 'Background', 'fg', 'bg']


class Graphic(object):
    '''
    Compose a Select Graphic Rendition (SGR) ANSI escape sequence.
    '''

    def __init__(self, *values):
        self.values = values
        self.sequence = sequence('m', fields=-1)(*values)

    def __add__(self, their):
        if isinstance(their, basestring):
            return ''.join([str(self), their])
        else:
            return Graphic(*(self.values + their.values))

    def __call__(self, text, reset=True):
        result = self.sequence + text
        if reset:
            result += str(Graphic('0'))
        return result

    def __str__(self):
        return self.sequence


# Effects
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


# Colours
class Foreground(object):
    '''
    ANSI foreground colours.
    '''

    black           = Graphic('30')
    red             = Graphic('31')
    green           = Graphic('32')
    brown           = Graphic('33')
    blue            = Graphic('34')
    magenta         = Graphic('35')
    cyan            = Graphic('36')
    grey            = Graphic('37')
    gray            = grey                  # US English
    default         = Graphic('39')
    darkgrey        = bright + black
    darkgray        = darkgrey              # US English
    brightred       = bright + red
    brightgreen     = bright + green
    yellow          = bright + brown
    brightblue      = bright + blue
    brightmagenta   = bright + magenta
    brightcyan      = bright + cyan
    white           = bright + grey


class Background(object):
    '''
    ANSI background colours.
    '''
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


# Aliases
fg = Foreground
bg = Background


if __name__ == '__main__':
    for c in (fg, bg):
        for item in dir(c):
            if item.startswith('_'):
                continue
            print getattr(c, item)(item), reset
