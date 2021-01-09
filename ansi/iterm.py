import binascii
from ansi.sequence import osc

def _b64(data):
    if not isinstance(data, bytes):
        data = data.encode()
    return binascii.b2a_base64(data, newline=False).decode()

notification = osc(9)

def badge(msg):
    return osc(1337)(SetBadgeFormat = _b64(msg))

def image(data, name="unnamed", **kwargs):
    kwargs["inline"] = 1
    return osc(1337)("File=name=%s" % _b64(name), **kwargs)[:-1] + ':' + _b64(data) + '\a'

def cursor(shape):
    return osc(1337)(CursorShape=shape)

def cursorguide(on):
    if isinstance(on, bool):
        on = ['no','yes'][bool(on)]
    return osc(1337)(HighlightCursorLine=on)

def attention(on):
    if isinstance(on, bool):
        on = ['no','yes'][bool(on)]
    return osc(1337)(RequestAttention=on)
