""" ECOR 1051 Fall 2019

Test function for the invert filter in simple_Cimpl_filters.
Last edited: Nov. 16, 2019 (Edited comments. No changes to algorithms.)
"""

"""This file shows one way to unit test an image-processing filter.
The test function creates two small images. The first is the 'original' image
that is passed to the filter. The second is identical to the transformed image
that we expect the filter to return. The colours in the expected image weren't
obtained by passing 'original' to the filter - what if the filter has a bug?
Instead, they were calculated 'by hand', based on the filter's specification.
"""

from Cimpl import create_color, create_image, get_color, set_color

from .simple_Cimpl_filters import invert

def check_equal(description: str, outcome, expected) -> None:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.

    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.

    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        # The format method is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.

        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")

def test_invert() -> None:
    '''A test function for invert.

    >>> test_invert()
    '''
    # Create an image with three pixels. For testing the invert filter, I picked
    # (0, 0, 0) and (255, 255, 255) as two of the colours, because they are the
    # brightest and darkest colours (boundary cases). I picked (128, 127, 128)
    # as the third colour because it's a non-gray colour in the "middle" of the
    # set of RGB colour codes.

    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(128, 127, 128))
    set_color(original, 2, 0,  create_color(255, 255, 255))

    # Create an image that's identical to the one a correct implementation of
    # invert should produce when it is passed original.

    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(255, 255, 255))
    set_color(expected, 1, 0,  create_color(127, 128, 127))
    set_color(expected, 2, 0,  create_color(0, 0, 0))

    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.

    inverted = invert(original)
    for x, y, col in inverted:  # col is the Color object for the pixel @ (x,y).
                                # There's no need to unpack that object into
                                # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

test_invert()