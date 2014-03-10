ANSI
====

Various ANSI escape codes, used in moving the cursor in a text console or
rendering coloured text.


Example
-------

Print something in bold yellow on a red background:

    >>> from ansi.colour import fg, bg
    >>> from ansi.colour.fx import reset
    >>> msg = (bg.red, fg.yellow, 'Hello world!', reset)
    >>> print ''.join(map(str, msg))
    ...

If you like syntactic sugar, you may also do:

    >>> from ansi.colour import fg, bg
    >>> print bg.red(fg.yellow('Hello world!'))
    ...

Also, 256 RGB colours are supported:

    >>> from ansi.colour.rgb import rgb256
    >>> from ansi.colour.fx import reset
    >>> msg = (rgb256(0xff, 0x80, 0x00), 'hello world', reset)
    >>> print ''.join(map(str, msg))
    ...

If you prefer to use American English instead:

    >>> from ansi.color import ...
    

References
----------

http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf
