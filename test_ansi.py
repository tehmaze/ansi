# noinspection PyUnresolvedReferences
import pytest


def test_import() -> None:
    """Test that importing works for all levels."""
    import ansi
    import ansi.colour
    from ansi.colour import bg, fg, fx, rgb
    from ansi.colour.fx import reset
    from ansi.colour.rgb import rgb256


# noinspection PyUnresolvedReferences
def test_import_color() -> None:
    """Test that importing works for the color spelling too."""
    import ansi
    import ansi.color
    from ansi.color import bg, fg, fx, rgb
    from ansi.color.fx import reset
    from ansi.color.rgb import rgb256


def test_fg_bg() -> None:
    from ansi.colour import fg, bg
    from ansi.colour.fx import reset
    msg = (bg.red, fg.yellow, 'Hello world!', reset)
    assert ''.join(map(str, msg)) == '\x1b[41m\x1b[33mHello world!\x1b[0m'


def test_sugar() -> None:
    from ansi.colour import fg, bg
    assert bg.red(fg.yellow('Hello world!')) == \
           '\x1b[41m\x1b[33mHello world!\x1b[0m\x1b[0m'


def test_rgb() -> None:
    from ansi.colour.rgb import rgb256
    from ansi.colour.fx import reset
    msg = (rgb256(0xff, 0x80, 0x00), 'hello world', reset)
    assert ''.join(map(str, msg)) == '\x1b[38;5;214mhello world\x1b[0m'


def test_osc() -> None:
    from ansi import osc
    assert osc.windowtitle('title') == '\x1b]0;title\x07'


def test_iterm() -> None:
    from ansi import iterm
    assert iterm.attention(True) == '\x1b]1337;RequestAttention=yes\x07'
    assert iterm.attention('yes') == '\x1b]1337;RequestAttention=yes\x07'


def test_add() -> None:
    from ansi.colour import fg
    assert (fg.blue + fg.bold)('x') == '\x1b[34;1mx\x1b[0m'

def test_add_to_string() -> None:
    from ansi.colour import fg, fx
    assert fg.blue + 'x' == '\x1b[34mx'
    assert fg.blue + 'x' + fx.reset == '\x1b[34mx\x1b[0m'

def test_add_other() -> None:
    from ansi.colour import fg, fx
    with pytest.raises(TypeError):
        fg.blue + 1

    with pytest.raises(TypeError):
        1 + fg.blue

def test_empty() -> None:
    from ansi.colour import fg, fx
    assert fg.none('12') == '12'
    assert fg.none + '12' == '12'
    assert fx.noop + '12' == '12'
