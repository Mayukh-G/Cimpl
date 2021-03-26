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
    # Testing horizontal symmetry
    test_img = Image(width=2, height=2)
    test_img.set_color(0, 0, Color(0, 0, 0))
    test_img.set_color(0, 1, Color(0, 0, 0))
    # The other pixels are already white by default

    expected = Image(width=2, height=2)
    expected.set_color(0, 0, Color(0, 0, 0))
    expected.set_color(0, 1, Color(0, 0, 0))

    res = flip_horizontal(test_img)
    for x, y, col in res:
        check_equal(f"Testing if pixels reminded the same in an image with horizontal symmetry at pixel {x, y}",
                    col, expected.get_color(x, y))

    # Testing Vertical symmetry
    test_img = Image(width=2, height=2)
    test_img.set_color(0, 0, Color(255, 255, 255))
    test_img.set_color(0, 1, Color(0, 0, 0))
    test_img.set_color(1, 0, Color(255, 255, 255))
    test_img.set_color(1, 1, Color(0, 0, 0))

    expected = Image(width=2, height=2)
    expected.set_color(0, 0, Color(0, 0, 0))
    expected.set_color(0, 1, Color(255, 255, 255))
    expected.set_color(1, 0, Color(0, 0, 0))
    expected.set_color(1, 1, Color(255, 255, 255))

    res = flip_horizontal(test_img)
    for x, y, col in res:
        check_equal(f"Testing if pixels in an image with horizontal symmetry {x, y}",
                    col, expected.get_color(x, y))


if __name__ == '__main__':
    horizontal_check()
