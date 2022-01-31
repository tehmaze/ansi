ANSI Changelog
==============

Various ANSI escape codes, used in moving the cursor in a text console or
rendering coloured text.

0.3.5
-----
- [PR #21](https://github.com/tehmaze/ansi/pull/21) use 3rd party
  `typing_extensions` module for better version compatibility

0.3.4
-----

- Three minor versions were briefly released to resolve packaging/README issues
  with 0.3.1.

0.3.1
-----
- [PR #18](https://github.com/tehmaze/ansi/pull/14) Deprecate Python 2 and
  versions earlier than 3.7 by adding type information. `rgb()` function no
  longer accepts strings of integers, only integers.
- [PR #14](https://github.com/tehmaze/ansi/pull/14) Add support for 8 and 24-bit
  True Color.

0.3.0 
-----
- Broken, due to a configuration error this package is not installable

0.2.0
-----

- [PR #13](https://github.com/tehmaze/ansi/pull/13) Support for OSC and some
  proprietary iTerm sequences
- [PR #12](https://github.com/tehmaze/ansi/pull/13) show/hide cursor sequence
