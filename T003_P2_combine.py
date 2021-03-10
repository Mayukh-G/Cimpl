# Author : Mayukh Gautam
# Number : 101181018
# Course : ECOR1042G
from Cimpl import Image, Color, show
from unit_testing import check_equal


def combine(img_r: Image, img_g: Image, img_b: Image) -> Image:
    """
    Takes in three Cimpl Image objects of matching dimentions. One filtered red, one filtered green, and one filtered
    blue. Verifies if the arguments passed in are of the correct type, then combines the three filtered images into one final
    image.

    Returns None if passed arguments are unexpected or if dimentions do not match.
    If not, returns the combined Cimpl Image object

    >>> combine(r, g, b)
    <Image object at (Memory Address)>

    >>> combine(r, g, 1)
    None

    >>> combine(1, 2, 3)
    None
    """
    if not isinstance(img_r, Image) or not isinstance(img_g, Image) or not isinstance(img_b, Image):
        # noinspection PyTypeChecker
        return None
    if not (
            img_r.get_width() == img_b.get_width() == img_g.get_width() and img_r.get_height() == img_b.get_height() == img_g.get_height()):
        # noinspection PyTypeChecker
        return None

    final_img = Image(height=img_r.get_height(), width=img_r.get_width())
    for i in range(img_r.get_width()):
        for j in range(img_r.get_height()):
            colour = Color(img_r.get_color(i, j)[0], img_g.get_color(i, j)[1], img_b.get_color(i, j)[2])
            final_img.set_color(i, j, colour)
    return final_img


def combine_test(red_img: Image = None, green_img: Image = None, blue_img: Image = None) -> None:
    """
    Checks if the provided filtered images combine into the correct final image.
    If no images are passed in as arguments, or if at least one argument is ignored. Instead checks if combine() passes
    boundary test cases.

    Check Spesific filtered images
    >>> combine_test(r, g, b)

    Check edge cases
    >>> combine_test()

    """
    if red_img is None or blue_img is None or green_img is None:
        # Small Values in each
        test_r, test_g, test_b = Image(width=2, height=2, color=Color(1, 1, 1)), \
                                 Image(width=2, height=2, color=Color(1, 1, 1)), \
                                 Image(width=2, height=2, color=Color(1, 1, 1))
        expect = Image(width=2, height=2, color=Color(1, 1, 1))
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
    else:
        output_img = combine(r, g, b)
        for i in range(output_img.get_width()):
            for j in range(output_img.get_height()):
                correct = Color(red_img.get_color(i, j)[0], green_img.get_color(i, j)[1], blue_img.get_color(i, j)[2])
                output_colour = output_img.get_color(i, j)
                check_equal(f"Checking pixel at {i, j}", output_colour, correct)


if __name__ == '__main__':
    # This directory is where the Images are stored feel free to change it to where they are in your system
    directory = "GroupProject/CimpL-Demo/"
    expected = Image(filename=directory + "p2-original.png")
    r = Image(filename=directory + "red_image.png")
    g = Image(filename=directory + "green_image.png")
    b = Image(filename=directory + "blue_image.png")
    final = combine(r, g, b)
    combine_test(r, g, b)
    combine_test()
    show(final)
