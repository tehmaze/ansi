def test_import():
    import ansi
    import ansi.colour
    import ansi.color
    from ansi.colour import bg, fg, fx, rgb
    from ansi.color import bg, fg, fx, rgb
    from ansi.colour.fx import reset
    from ansi.color.fx import reset
    from ansi.colour.rgb import rgb256
    from ansi.color.rgb import rgb256

def test_fg_bg():
    from ansi.colour import fg, bg
    from ansi.colour.fx import reset
    msg = (bg.red, fg.yellow, 'Hello world!', reset)
    assert ''.join(map(str, msg)) == '\x1b[41m\x1b[33mHello world!\x1b[0m'

def test_sugar():
    from ansi.colour import fg, bg
    assert bg.red(fg.yellow('Hello world!')) == \
        '\x1b[41m\x1b[33mHello world!\x1b[0m\x1b[0m'

def test_rgb():
    from ansi.colour.rgb import rgb256
    from ansi.colour.fx import reset
    msg = (rgb256(0xff, 0x80, 0x00), 'hello world', reset)
    assert ''.join(map(str, msg)) == '\x1b[38;5;214mhello world\x1b[0m'
