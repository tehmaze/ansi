# noinspection PyUnresolvedReferences
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
