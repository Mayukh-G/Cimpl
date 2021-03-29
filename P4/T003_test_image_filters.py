# Group  : T003
# Course : ECOR1042G
# Number : 101195221, 101181018, 101178559, 101185138
# Names  : Jacob Ridgway, Mayukh Gautam, Alex Watson, Alexander Christie

from Cimpl import *
from T003_image_filters import *
from unit_testing import check_equal


def test_extreme() -> None:  # Jacob Ridgway
    """
    Test function for extreme contrast filter.

    >>> test_extreme()
    """

    original = create_image(3, 1)
    set_color(original, 0, 0, create_color(160, 230, 40))
    set_color(original, 1, 0, create_color(225, 10, 130))
    set_color(original, 2, 0, create_color(20, 100, 255))

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(255, 255, 0))
    set_color(expected, 1, 0, create_color(255, 0, 255))
    set_color(expected, 2, 0, create_color(0, 0, 255))

    actual_filtered_image = extreme_contrast(original)

    for x, y, col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_posterize() -> None:  # Alexander Christie
    '''
    tests the posterize filter function
    >>> test_posterize()
    '''
    original = create_image(3, 2)
    set_color(original, 0, 0, create_color(64, 64, 64))
    set_color(original, 1, 0, create_color(191, 191, 191))
    set_color(original, 2, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(255, 255, 255))
    set_color(original, 1, 1, create_color(31, 95, 159))
    set_color(original, 2, 1, create_color(65, 233, 111))
    expected = create_image(3, 2)
    set_color(expected, 0, 0, create_color(95, 95, 95))
    set_color(expected, 1, 0, create_color(159, 159, 159))
    set_color(expected, 2, 0, create_color(31, 31, 31))
    set_color(expected, 0, 1, create_color(223, 223, 223))
    set_color(expected, 1, 1, create_color(31, 95, 159))
    set_color(expected, 2, 1, create_color(95, 223, 95))

    posterized_image = posterize_filter(original)

    for x, y, col in posterized_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_sepia() -> None:  # Alex Watson
    """
    A test function for sepia.

    >>>test_sepia()

    """
    original = create_image(3, 1)  # Creating an original image to be tested  by the sepia filter.
    set_color(original, 0, 0, create_color(45, 67, 233))
    set_color(original, 1, 0, create_color(120, 27, 38))
    set_color(original, 2, 0, create_color(255, 237, 154))

    expected1 = create_image(3, 1)
    set_color(expected1, 0, 0, create_color(132, 115, 97))  # Medium gray
    set_color(expected1, 1, 0, create_color(67, 61, 54))  # Light gray
    set_color(expected1, 2, 0, create_color(232, 215, 199))  # Dark gray

    sepia_test = sepia_filter(original)
    for x, y, col in sepia_test:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected1, x, y))


BLOOD_C = (255, 0, 0)
LEMON_C = (255, 255, 0)
PINK_C = (255, 0, 255)


def check_three_tone() -> None:  # Mayukh Gautam
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


def test_draw() -> None:  # Alex Watson
    """
    Tests the draw filter.

    >>>test_draw()
    """

    original = create_image(20, 20)  # creating a blank 20x20 image
    test_curve = draw_curve(original, "blue", [(0, 0), (10, 10), (20, 20)])

    expected = create_image(20, 20)  # creates a blank image for expected
    for i in range(20):
        set_color(expected, i, i, create_color(0, 0, 255))  # sets diagonal line downwards in expected
        for j in range(i - 4, i + 5):  # adds coloured pixels +/- 4 from line
            if j in range(20):  # ensures they do not draw out of image
                set_color(expected, i, j, create_color(0, 0, 255))
    for x, y, col in test_curve[0]:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))

    # Testing Return Points
    expected_return_points = [(0, 0), (20, 20)]
    if expected_return_points == test_curve[1]:
        result = "PASSED"
    else:
        result = "FAILED"
    print("Checking return points: ", result)
    print("Expected: ", expected_return_points, ", got: ", test_curve[1])


def test_edge_detection() -> None:  # Jacob Ridgway
    '''
    Tests edge detection function.
    '''

    original = create_image(3, 3)
    set_color(original, 0, 0, create_color(60, 78, 120))  # First row, xpos 1
    set_color(original, 1, 0, create_color(82, 55, 210))  # xpos 2
    set_color(original, 2, 0, create_color(45, 56, 34))  # xpos 3

    set_color(original, 0, 1, create_color(60, 78, 120))  # Second row, xpos 1
    set_color(original, 1, 1, create_color(67, 23, 230))  # xpos 2
    set_color(original, 2, 1, create_color(45, 56, 34))  # xpos 3

    set_color(original, 0, 2, create_color(23, 255, 130))  # These are on the bottom of the image
    set_color(original, 1, 2, create_color(56, 234, 210))
    set_color(original, 2, 2, create_color(55, 45, 120))

    expected = create_image(3, 3)
    set_color(expected, 0, 0, create_color(255, 255, 255))  # First row, xpos 1, Using threshold of 1
    set_color(expected, 1, 0, create_color(0, 0, 0))  # xpos 2
    set_color(expected, 2, 0, create_color(255, 255, 255))  # xpos 3

    set_color(expected, 0, 1, create_color(0, 0, 0))  # Second row, xpos 1
    set_color(expected, 1, 1, create_color(0, 0, 0))  # xpos 2
    set_color(expected, 2, 1, create_color(0, 0, 0))  # xpos 3

    set_color(expected, 0, 2, create_color(255, 255, 255))  # Bottom pixels get set to white
    set_color(expected, 1, 2, create_color(255, 255, 255))
    set_color(expected, 2, 2, create_color(255, 255, 255))

    actual_filtered_image = detect_edges(original, 1)

    for x, y, col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def horizontal_check() -> None: # Mayukh Gautam
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


def test_vertical_flip() -> None:  # Alexander Christie
    '''
    tests that the pixls change positions properly in the vertical_flip filter.
    >>> test_posterize()
    '''
    original = create_image(3, 3)
    set_color(original, 0, 0, create_color(1, 1, 1))
    set_color(original, 1, 0, create_color(255, 0, 3))
    set_color(original, 2, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(255, 255, 255))
    set_color(original, 1, 1, create_color(31, 95, 159))
    set_color(original, 2, 1, create_color(65, 233, 111))
    set_color(original, 0, 2, create_color(0, 0, 0))
    set_color(original, 1, 2, create_color(10, 10, 10))
    set_color(original, 2, 2, create_color(31, 31, 31))
    expected = create_image(3, 3)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(10, 10, 10))
    set_color(expected, 2, 0, create_color(31, 31, 31))
    set_color(expected, 0, 1, create_color(255, 255, 255))
    set_color(expected, 1, 1, create_color(31, 95, 159))
    set_color(expected, 2, 1, create_color(65, 233, 111))
    set_color(expected, 0, 2, create_color(1, 1, 1))
    set_color(expected, 1, 2, create_color(255, 0, 3))
    set_color(expected, 2, 2, create_color(0, 0, 0))

    fliped_image = flip_vertical(original)

    for x, y, col in fliped_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


if __name__ == '__main__':
    print("\t--- Extreme contrast ---\n")
    test_extreme()
    print("\t--- Posterize ---\n")
    test_posterize()
    print("\t--- Sepia ---\n")
    test_sepia()
    print("\t--- Three Tone ---\n")
    check_three_tone()

    print("\t--- Draw Curve ---\n")
    test_draw()
    print("\t--- Edge detection ---\n")
    test_edge_detection()
    print("\t--- Horizontal flip ---\n")
    horizontal_check()
    print("\t--- Vertical flip ---\n")
    test_vertical_flip()

