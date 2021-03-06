# -*- coding: utf-8 -*-

"""
Unittests for the core module
"""

from escape.core import Escape


def test_string_gets_styled_black():
    assert Escape('hello').black() == '\x1b[30mhello\x1b[39m'


def test_string_gets_styled_red():
    assert Escape('hello').red() == '\x1b[31mhello\x1b[39m'


def test_string_gets_styled_bright_red():
    assert Escape('hello').bright_red() == '\x1b[91mhello\x1b[39m'


def test_string_gets_styled_green():
    assert Escape('hello').green() == '\x1b[32mhello\x1b[39m'


def test_string_gets_styled_bright_green():
    assert Escape('hello').bright_green() == u'\x1b[92mhello\x1b[39m'


def test_string_gets_styled_yellow():
    assert Escape('hello').yellow() == '\x1b[33mhello\x1b[39m'


def test_string_gets_styled_bright_yellow():
    assert Escape('hello').bright_yellow() == '\x1b[93mhello\x1b[39m'


def test_string_gets_styled_blue():
    assert Escape('hello').blue() == '\x1b[34mhello\x1b[39m'


def test_string_gets_styled_bright_blue():
    assert Escape('hello').bright_blue() == '\x1b[94mhello\x1b[39m'


def test_string_gets_styled_magenta():
    assert Escape('hello').magenta() == '\x1b[35mhello\x1b[39m'


def test_string_gets_styled_bright_magenta():
    assert Escape('hello').bright_magenta() == '\x1b[95mhello\x1b[39m'


def test_string_gets_styled_cyan():
    assert Escape('hello').cyan() == '\x1b[36mhello\x1b[39m'


def test_string_gets_styled_bright_cyan():
    assert Escape('hello').bright_cyan() == '\x1b[96mhello\x1b[39m'


def test_string_gets_styled_white():
    assert Escape('hello').white() == '\x1b[37mhello\x1b[39m'


def test_string_gets_styled_bright_white():
    assert Escape('hello').bright_white() == '\x1b[97mhello\x1b[39m'


def test_string_gets_styled_gray():
    assert Escape('hello').gray() == '\x1b[90mhello\x1b[39m'


def test_string_gets_styled_black_background():
    assert Escape('hello').black_background() == '\x1b[40mhello\x1b[49m'


def test_string_gets_styled_bright_black_background():
    assert Escape('hello').bright_black_background() == '\x1b[100mhello\x1b[49m'


def test_string_gets_styled_red_background():
    assert Escape('hello').red_background() == '\x1b[41mhello\x1b[49m'


def test_string_gets_styled_bright_red_background():
    assert Escape('hello').bright_red_background() == '\x1b[101mhello\x1b[49m'


def test_string_gets_styled_green_background():
    assert Escape('hello').green_background() == '\x1b[42mhello\x1b[49m'


def test_string_gets_styled_bright_green_background():
    assert Escape('hello').bright_green_background() == '\x1b[102mhello\x1b[49m'


def test_string_gets_styled_yellow_background():
    assert Escape('hello').yellow_background() == '\x1b[43mhello\x1b[49m'


def test_string_gets_styled_bright_yellow_background():
    assert Escape('hello').bright_yellow_background() == '\x1b[103mhello\x1b[49m'


def test_string_gets_styled_blue_background():
    assert Escape('hello').blue_background() == '\x1b[44mhello\x1b[49m'


def test_string_gets_styled_bright_blue_background():
    assert Escape('hello').bright_blue_background() == '\x1b[104mhello\x1b[49m'


def test_string_gets_styled_magenta_background():
    assert Escape('hello').magenta_background() == '\x1b[45mhello\x1b[49m'


def test_string_gets_styled_bright_magenta_background():
    assert Escape('hello').bright_magenta_background() == '\x1b[105mhello\x1b[49m'


def test_string_gets_styled_cyan_background():
    assert Escape('hello').cyan_background() == '\x1b[46mhello\x1b[49m'


def test_string_gets_styled_bright_cyan_background():
    assert Escape('hello').bright_cyan_background() == '\x1b[106mhello\x1b[49m'


def test_string_gets_styled_white_background():
    assert Escape('hello').white_background() == '\x1b[47mhello\x1b[49m'


def test_string_gets_styled_bright_white_background():
    assert Escape('hello').bright_white_background() == '\x1b[107mhello\x1b[49m'


def test_string_gets_styled_bold():
    assert Escape('hello').bold() == '\x1b[1mhello\x1b[22m'


def test_string_gets_styled_dim():
    assert Escape('hello').dim() == '\x1b[2mhello\x1b[22m'


def test_string_gets_styled_italic():
    assert Escape('hello').italic() == '\x1b[3mhello\x1b[23m'


def test_string_gets_styled_inverse():
    assert Escape('hello').inverse() == '\x1b[7mhello\x1b[27m'


def test_string_gets_hidden():
    assert Escape('hello').hidden() == '\x1b[8mhello\x1b[28m'


def test_string_gets_striked_through():
    assert Escape('hello').strikethrough() == '\x1b[9mhello\x1b[29m'


def test_string_gets_underlined():
    assert Escape('hello').underline() == '\x1b[4mhello\x1b[24m'


def test_multiple_styles_get_applied():
    assert Escape('Hello World').red().blue() == '\x1b[34m\x1b[31mHello World\x1b[39m\x1b[39m'


def test_conatenate_with_other_strings():
    assert Escape('hello') + ' world' == 'hello world'
    assert 'world,' + Escape('Hi!').green() == 'world,\x1b[32mHi!\x1b[39m'


def test_styles_get_nested():
    assert (Escape('Hello ' + Escape('World')
                   .bright_green_background())
            .bright_red()) == '\x1b[91mHello \x1b[102mWorld\x1b[49m\x1b[39m'


def test_length_returns_length_of_unstyled_string():
    assert len(Escape('Hello').red()) == len('Hello')


def test_multiply_creates_repeated_styled_string():
    assert Escape('red').red() * 3 == '\x1b[31mred\x1b[39m\x1b[31mred\x1b[39m\x1b[31mred\x1b[39m'


def test_using_unicode_codepoints_does_not_raise():
    Escape(u'\u0150 ', Escape('Hello').bright_green_background()).bright_red()
