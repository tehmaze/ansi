import binascii
from typing import Any, Union

from ansi.sequence import osc


def _b64(data: Union[bytes, str]) -> str:
    if not isinstance(data, bytes):
        data = data.encode()
    return binascii.b2a_base64(data, newline=False).decode()


notification = osc(9)


def badge(msg: str) -> str:
    return osc(1337)(SetBadgeFormat=_b64(msg))


def image(data: str, name: str = "unnamed", **kwargs: Any) -> str:
    kwargs["inline"] = 1
    return osc(1337)("File=name=%s" % _b64(name), **kwargs)[:-1] + ':' + _b64(data) + '\a'


def cursor(shape: str) -> str:
    return osc(1337)(CursorShape=shape)


def cursorguide(on: Union[bool, str]) -> str:
    if isinstance(on, bool):
        on = ['no', 'yes'][on]
    return osc(1337)(HighlightCursorLine=on)


def attention(on: Union[bool, str]) -> str:
    if isinstance(on, bool):
        on = ['no', 'yes'][on]
    return osc(1337)(RequestAttention=on)
