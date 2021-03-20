# Author : Mayukh Gautam
# Number : 101181018
# Course : ECOR1042G
# Group  : T003

from T003_P3_filter_three_tone import three_tone
from Cimpl import *
from unit_testing import check_equal
BLOOD_C = (255, 0, 0)
LEMON_C = (255, 255, 0)
PINK_C = (255, 0, 255)


def check_three_tone() -> None:
    """
    Tests the function three_tone. Tests string association, border values, and non-integer brightness
    Prints the results of the tests.

    >>> check_three_tone()
    None
    """
    # Checking string association, with colours
    img_test = Image(width=2, height=2)
    img_test.set_color(0, 0, Color(1, 1, 1))
    img_test.set_color(0, 1, Color(100, 100, 100))
    img_test.set_color(1, 0, Color(180, 180, 180))

    expected = Image(width=2, height=2)
    expected.set_color(0, 0, Color(*BLOOD_C))
    expected.set_color(0, 1, Color(*LEMON_C))
    expected.set_color(1, 0, Color(*PINK_C))
    expected.set_color(1, 1, Color(*PINK_C))

    res = three_tone("blood", "lemon", "pink", img_test)
    for i, j, col in res:
        check_equal(f"Checking String association with colors at pixel {i, j}", col, expected.get_color(i, j))

    # Checking Border cases. Transition values 85, 170
    img_test = Image(width=1, height=2)
    img_test.set_color(0, 0, Color(85, 85, 85))
    img_test.set_color(0, 1, Color(171, 171, 171))

    expected = Image(width=1, height=2)
    expected.set_color(0, 0, Color(*LEMON_C))
    expected.set_color(0, 1, Color(*PINK_C))

    res = three_tone("blood", "lemon", "pink", img_test)
    for i, j, col in res:
        check_equal(f"Checking Border cases at pixel {i, j}", col, expected.get_color(i, j))

    # Non-integer average brightness
    img_test = Image(width=1, height=2, color=Color(255, 10, 12))
    img_test.set_color(0, 1, Color(100, 100, 102))

    expected = Image(width=1, height=2)
    expected.set_color(0, 0, Color(*LEMON_C))
    expected.set_color(0, 1, Color(*LEMON_C))

    res = three_tone("blood", "lemon", "pink", img_test)
    for i, j, col in res:
        check_equal(f"Checking non-integer brightness at pixel {i, j}", col, expected.get_color(i, j))


if __name__ == '__main__':
    check_three_tone()

