from typing import Tuple

from ansi.sequence import sequence

RGB = Tuple[int, int, int]

ANSI_COLOURS = (
    (0x00, 0x00, 0x00), (0xcd, 0x00, 0x00),
    (0x00, 0xcd, 0x00), (0xcd, 0xcd, 0x00),
    (0x00, 0x00, 0xee), (0xcd, 0x00, 0xcd),
    (0x00, 0xcd, 0xcd), (0xe5, 0xe5, 0xe5),
    (0x7f, 0x7f, 0x7f), (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00), (0xff, 0xff, 0x00),
    (0x5c, 0x5c, 0xff), (0xff, 0x00, 0xff),
    (0x00, 0xff, 0xff), (0xff, 0xff, 0xff),
)


def rgb_distance(rgb1: RGB, rgb2: RGB) -> int:
    """
    Calculate the distance between two RGB sequences.
    """
    return sum(map(lambda c: (c[0] - c[1]) ** 2,
                   zip(rgb1, rgb2)))


def rgb_reduce(r: int, g: int, b: int, mode: int = 8) -> str:
    """
    Convert an RGB colour to 8 or 16 colour ANSI graphics.

    Finds the closest color within the 8 or 16 color palette to a given RGB value.
    """
    assert mode in (8, 16), 'Mode has to be 8 or 16, got %r instead.' % mode
    colours = ANSI_COLOURS[:mode]
    matches = [(rgb_distance(c, (r, g, b)), i)
               for i, c in enumerate(colours)]
    matches.sort()
    return sequence('m')(str(30 + matches[0][1]))


def rgb8(r: int, g: int, b: int) -> str:
    """
    Convert an RGB colour to 8 colour ANSI graphics.

    Finds the closest color within the 8 color palette to a given RGB value.
    """
    return rgb_reduce(r, g, b, 8)


def rgb16(r: int, g: int, b: int) -> str:
    """
    Convert an RGB colour to 16 colour ANSI graphics.

    Finds the closest color within the 16 color palette to a given RGB value.
    """
    return rgb_reduce(r, g, b, 16)


def rgb256(r: int, g: int, b: int, bg: bool=False) -> str:
    """
    Convert an RGB colour to 256 colour ANSI graphics.

    Finds the closest color within the 256 color palette to a given RGB value.
    """
    grey = False
    poss = True
    step = 2.5

    while poss:  # As long as the colour could be grey scale
        if r < step or g < step or b < step:
            grey = r < step and g < step and b < step
            poss = False

        step += 42.5

    if grey:
        colour = 232 + int(float(sum([r, g, b]) / 33.0))
    else:
        colour = sum([16] + [int(6 * float(val) / 256) * mod
                             for val, mod in ((r, 36), (g, 6), (b, 1))])

    return sequence('m', fields=3)(38 if not bg else 48, 5, colour)
