# Author : Mayukh Gautam
# Number : 101181018
import GroupProject.Cimpl as Cimpl


def combine(img_r: Cimpl.Image, img_g: Cimpl.Image, img_b: Cimpl.Image) -> Cimpl.Image:
    """
    Takes in three Cimpl Image objects of matching dimentions. One filtered red, one filtered green, and one filtered
    blue. Verifies if the arguments passed in are of the correct type, then combines the three filtered images into one final
    image.

    Returns None if passed arguments are unexpected or if dimentions do not match.
    If not, returns the combined Cimpl Image object

    >>> combine(r, g, b)
    <GroupProject.Cimpl.Image object at (Memory Address)>

    >>> combine(r, g, 1)
    None

    >>> combine(1, 2, 3)
    None
    """
    if not isinstance(img_r, Cimpl.Image) or not isinstance(img_g, Cimpl.Image) or not isinstance(img_b, Cimpl.Image):
        # noinspection PyTypeChecker
        return None
    if not (img_r.get_width() == img_b.get_width() == img_g.get_width() and img_r.get_height() == img_b.get_height() == img_g.get_height()):
        # noinspection PyTypeChecker
        return None

    final = Cimpl.Image(height=img_r.get_height(), width=img_r.get_width())
    for i in range(img_r.get_width()):
        for j in range(img_r.get_height()):
            r_pix = img_r.get_color(i, j)[0]
            g_pix = img_g.get_color(i, j)[1]
            b_pix = img_b.get_color(i, j)[2]
            final.set_color(i, j, Cimpl.Color(r_pix, g_pix, b_pix))
    return final


if __name__ == '__main__':
    r = Cimpl.Image(filename="./CimpL-Demo/red_image.png")
    g = Cimpl.Image(filename="./CimpL-Demo/green_image.png")
    b = Cimpl.Image(filename="./CimpL-Demo/blue_image.png")
    final = combine(r, g, b)
    Cimpl.show(final)

