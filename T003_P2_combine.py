# Author : Mayukh Gautam
# Number : 101181018
# Course : ECOR1042G
from Cimpl import Image, Color, show, choose_file
from unit_testing import check_equal


def combine(img_1: Image, img_2: Image, img_3: Image) -> Image:
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


def combine_test() -> None:
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
    # Will prompt user to select three files.
    # try, except used to avoid crashes
    err = True
    while err:
        try:
            img1 = Image(filename=choose_file())
            img2 = Image(filename=choose_file())
            img3 = Image(filename=choose_file())
            err = False
        except AttributeError:
            print("** Please select Three image files to serve as filtered images for the combine function\n"
                  "Each Time you see this you must re select three images **")

    final = combine(img1, img2, img3)
    combine_test()
    show(final)
