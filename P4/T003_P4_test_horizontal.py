# Author : Mayukh Gautam
# Number : 101181018
# Course : ECOR1042G
# Group  : T003
from Cimpl import *
from unit_testing import check_equal
from T003_P4_filter_horizontal import flip_horizontal


def horizontal_check() -> None:
    """
    Testing if pixels are switch properly in horizontal_flip

    >>> horizontal_check()
    None
    """
    # Tests if pixels go where they are supposed to and if pixels in the middle stay in the middle
    test_img = Image(width=3, height=3)
    test_img.set_color(0, 0, Color(0, 0, 0))  # 0 1 1
    test_img.set_color(1, 1, Color(0, 0, 0))  # 1 0 1
    test_img.set_color(0, 2, Color(0, 0, 0))  # 0 1 1

    # The other pixels are already white by default

    expected = Image(width=3, height=3)
    expected.set_color(2, 0, Color(0, 0, 0))  # 1 1 0
    expected.set_color(1, 1, Color(0, 0, 0))  # 1 0 1
    expected.set_color(2, 2, Color(0, 0, 0))  # 1 1 0

    res = flip_horizontal(test_img)
    for x, y, col in res:
        check_equal(f"Testing if pixels at {x, y}",
                    col, expected.get_color(x, y))


if __name__ == '__main__':
    horizontal_check()
