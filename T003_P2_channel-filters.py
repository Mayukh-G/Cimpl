# Group  : T003
# Course : ECOR1042G
# Number : 101195221, 101181018, 101178559, 101185138
# Names  : Jacob Ridgway, Mayukh Gautam, Alex Watson, Alexander Christie

from Cimpl import *
from unit_testing import check_equal


def blue_filter(image: Image) -> Image:   # Author: Jacob Ridgway
    """
    Returns a copy of original image with the red and green channels removed,
    leaving only the blue channel.

    >>> file = choose_file()
    >>> image = load_image(file)
    >>> blue_filtered_image = blue_filter(image)
    >>> show(blue_filtered_image)
    """

    new_image = copy(image)
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        new_colour = create_color(0, 0, b)
        set_color(new_image, x, y, new_colour)

    return new_image


def test_blue_filter() -> None:  # Author: Jacob Ridgway
    """
    Tests the blue_filter function.

    >>> test_blue_filter()
    """

    original = create_image(3, 1)
    set_color(original, 0, 0, create_color(90, 120, 60))
    set_color(original, 1, 0, create_color(234, 250, 255))
    set_color(original, 2, 0, create_color(255, 80, 210))

    expected = create_image(3, 1)
    set_color(expected, 0, 0, create_color(0, 0, 60))
    set_color(expected, 1, 0, create_color(0, 0, 255))
    set_color(expected, 2, 0, create_color(0, 0, 210))

    actual_filtered_image = blue_filter(original)

    for x, y, col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def green_filter(image: Image) -> Image:  # Author: Alex Watson
    """
    Returns a copy of image; that is, an image that only contains the green
    components of the original image.

    >>> image = load_image(choose_file())
    >>> green_filtered = green_filter(image)
    >>> show(green_filtered)
    """

    new_image = copy(image)
    for x, y, (r, g, b) in image:
        green = create_color(0, g, 0)
        set_color(new_image, x, y, green)
    return new_image


def test_green_filter() -> None: # Author: Alex Watson
    """
    A test function for green_filter.

    >>>test_green_filter()
    """
    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(1, 10, 5))
    set_color(original, 1, 0, create_color(13, 120, 55))
    set_color(original, 2, 0, create_color(125, 255, 79))
    set_color(original, 3, 0, create_color(179, 135, 210))
    set_color(original, 4, 0, create_color(30, 0, 200))
    set_color(original, 5, 0, create_color(230, 155, 65))
    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 10, 0))
    set_color(expected, 1, 0, create_color(0, 120, 0))
    set_color(expected, 2, 0, create_color(0, 255, 0))
    set_color(expected, 3, 0, create_color(0, 135, 0))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    set_color(expected, 5, 0, create_color(0, 155, 0))
    green_test = green_filter(original)
    for x, y, col in green_test:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def red_channel(image: Image) -> Image:  # Author: Alexander Christie
    '''
    Returns a copy of the image as a new image containing only the red component
    of the original r,g,b color.
    >>> image = choose_file()
    >>>show(image)
    >>> red_image = red_channel(image)
    >>>show(red_image)

    '''
    duplicate = copy(image)
    for pixle in duplicate:
        x, y, (r, g, b) = pixle
        new_color = create_color(r, 0, 0)
        set_color(duplicate, x, y, new_color)
    return duplicate


def test_red_channel() -> None:  # Author: Alexander Christie
    '''
    Test the red_channel function using the check_equal function
    '''
    original = create_image(3, 2)
    set_color(original, 0, 0, create_color(125, 125, 125))
    set_color(original, 1, 0, create_color(255, 255, 255))
    set_color(original, 2, 0, create_color(0, 0, 0))
    set_color(original, 0, 1, create_color(75, 13, 150))
    set_color(original, 1, 1, create_color(245, 19, 0))
    set_color(original, 2, 1, create_color(90, 0, 16))
    expected = create_image(3, 2)
    set_color(expected, 0, 0, create_color(125, 0, 0))
    set_color(expected, 1, 0, create_color(255, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 0, 1, create_color(75, 0, 0))
    set_color(expected, 1, 1, create_color(245, 0, 0))
    set_color(expected, 2, 1, create_color(90, 0, 0))

    test_red_channel = red_channel(original)

    for x, y, col in test_red_channel:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def combine(img_1: Image, img_2: Image, img_3: Image) -> Image:  # Author : Mayukh Gautam
    """
    Takes in three Cimpl Image objects of matching dimentions. One filtered red, one filtered green, and one filtered
    blue. Verifies if the arguments passed in are of the correct type, then combines the three filtered images into one final
    image.

    Returns None if passed arguments are unexpected or if dimentions do not match.
    If not, returns the combined Cimpl Image object

    >>> combine(img1, img2, img3)
    <Image object at (Memory Address)>

    >>> combine(img1, img2, 1)
    None

    >>> combine(1, 2, 3)
    None
    """
    if not isinstance(img_1, Image) or not isinstance(img_2, Image) or not isinstance(img_3, Image):
        # noinspection PyTypeChecker
        return None
    if not (img_1.get_width() == img_2.get_width() == img_3.get_width() and img_1.get_height() == img_2.get_height() == img_3.get_height()):
        # noinspection PyTypeChecker
        return None

    final_img = Image(height=img_1.get_height(), width=img_1.get_width())
    for i in range(img_1.get_width()):
        for j in range(img_1.get_height()):
            colour_1, colour_2, colour_3 = img_1.get_color(i, j), img_2.get_color(i, j), img_3.get_color(i, j)
            r = (colour_1[0] + colour_2[0] + colour_3[0]) if (colour_1[0] + colour_2[0] + colour_3[0]) <= 255 else 255
            g = (colour_1[1] + colour_2[1] + colour_3[1]) if (colour_1[1] + colour_2[1] + colour_3[1]) <= 255 else 255
            b = (colour_1[2] + colour_2[2] + colour_3[2]) if (colour_1[2] + colour_2[2] + colour_3[2]) <= 255 else 255
            final_img.set_color(i, j, Color(r, g, b))
    return final_img


def combine_test() -> None:  # Author : Mayukh Gautam
    """
    Checks if combine() passes
    boundary test cases.

    Check edge cases
    >>> combine_test()
    None
    """
    # Small Values in each
    test_r, test_g, test_b = Image(width=2, height=2, color=Color(1, 1, 1)), \
                             Image(width=2, height=2, color=Color(1, 1, 1)), \
                             Image(width=2, height=2, color=Color(1, 1, 1))
    expect = Image(width=2, height=2, color=Color(3, 3, 3))
    output = combine(test_r, test_g, test_b)
    for i, j, col in output:
        check_equal(f"Edge case small value in red, green, blue at {i, j}", col, expect.get_color(i, j))

    # 255 in everything
    test_r, test_g, test_b = Image(width=2, height=2, color=Color(255, 255, 255)), \
                             Image(width=2, height=2, color=Color(255, 255, 255)), \
                             Image(width=2, height=2, color=Color(255, 255, 255))
    expect = Image(width=2, height=2, color=Color(255, 255, 255))
    output = combine(test_r, test_g, test_b)
    for i, j, col in output:
        check_equal(f"Edge case small value in red, green, blue at {i, j}", col, expect.get_color(i, j))

if __name__ == '__main__':
    # Main test script using all function
    original = Image(filename=choose_file())
    r_filtered = red_channel(original)
    b_filtered = blue_filter(original)
    g_filtered = green_filter(original)
    combined = combine(g_filtered, b_filtered, r_filtered)
    save_as(combined, "output-img-channel-filters.png")
