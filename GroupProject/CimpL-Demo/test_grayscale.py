""" ECOR 1051 Fall 2019

Test functions for function grayscale in simple_Cimpl_filters.
Last edited: Nov. 16, 2019
"""

from GroupProject.Cimpl import choose_file, create_color, create_image, get_color,\
                  set_color, load_image, Image

from .simple_Cimpl_filters import grayscale

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
    
def poor_test_grayscale1() -> None:
    '''A poorly designed test function for grayscale.
    
    This test function has at least two problems:
    
    (1) It verifies that each pixel's colour is a shade of gray, but it doesn't
    determine if it's the CORRECT shade of gray. For example, if grayscale() 
    returns an image in which all pixels were set to (128, 128, 128), regardless
    of the pixels' colours in the original image, the test would still pass
    because the condition:
         r != g or g != b
    would always be False.
    
    (2) The pixels in the original image are "random": they are competely
    dependant on where the camera was pointing when the photo was taken. 
    Suppose our grayscale filter has a bug, and doesn't correctly process any
    pixels that are already a shade of gray. If the original image doesn't have
    any gray pixels, the test function won't uncover this bug.

    >>> poor_test_grayscale1()
    '''
    image = load_image(choose_file())
    gray_image = grayscale(image)
    
    for x, y, (r, g, b) in gray_image:
        if r != g or g != b:
            print('FAIL: pixel @ ', (x, y), 'is', (r, g, b))
  
def poor_test_grayscale2() -> None:
    '''Another poorly designed test function for grayscale.
    
    This test function has at least two problems:
    
    (1) It attempts to fix problem (1) in the previous poorly designed test
    function. It gets the actual RGB values from a pixel in the image returned
    by grayscale, and compares them to the expected RGB values for that pixel;
    that is, the RGB values that a correct implementation of the filter should
    calculate.
    
    The problem is, what would happen if filter and the test function have the
    same bug in the code that calculates the RGB values. Suppose both functions 
    calculate each pixel's brightness this way:
    
        brightness = r + g + b // 3
    
    instead of using the correct expression:
    
        brightness = (r + g + b) // 3
    
    The test will pass, because the (incorrect) actual RGB values match the 
    (incorrect) expected values calculated by the test function.
    
    (2) Problem (2) is unchanged from the previous test function: we're testing
    random pixel colours.
    
    >>> poor_test_grayscale2()
    '''
    image = load_image(choose_file())
    gray_image = grayscale(image)
    
    for x, y, (r1, g1, b1) in gray_image:
        
        # r1, g1 and b1 are the ACTUAL RGB values of the pixel @ (x, y) in the
        # image returned by grayscale.
        
        # Calculate the EXPECTED RGB values for the pixel @ (x, y) in the
        # original image.
        
        r2, g2, b2 = get_color(image, x, y)
        brightness = (r2 + g2 + b2) // 3
        
        # Compare the actual and expected RGB values.
        if r1 != brightness or g1 != brightness or b1 != brightness:
            print('FAIL: pixel @ ', (x, y), 'is', (r1, g1, b1), 'not', 
                  (brightness, brightness, brightness))
 
def test_grayscale() -> None:  
    '''A test function for grayscale.
    
    >>> test_grayscale()
    '''
    # This test function checks if grayscale correctly transforms:
    # (0, 0, 0) to (0, 0, 0)  # the darkest gray shade
    # (0, 0, 1) to (0, 0, 0)  # the darkest non-gray shade
    # (127, 127, 127) to (127, 127, 127)  # a mid-range gray shade
    # (125, 73, 224) to (140, 140, 140)   # a non-gray colour
    # (254, 255, 255) to (254, 254, 254)  # the brightest non-gray shade  
    # (255, 255, 255) to (255, 255, 255)  # the brightest gray shade
    
    # Create an image with six pixels.
    
    original = create_image(6, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(0, 0, 1))
    set_color(original, 2, 0,  create_color(127, 127, 127))
    set_color(original, 3, 0,  create_color(125, 73, 224))
    set_color(original, 4, 0,  create_color(254, 255, 255))
    set_color(original, 5, 0,  create_color(255, 255, 255))
    
    # Create an image that's identical to the one a correct implementation of
    # grayscale should produce when it is passed original.
    
    expected = create_image(6, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(127, 127, 127))
    set_color(expected, 3, 0,  create_color(140, 140, 140))
    set_color(expected, 4, 0,  create_color(254, 254, 254))
    set_color(expected, 5, 0,  create_color(255, 255, 255))
       
    # Now compare the transformed image returned by the filter with the
    # expected image, one pixel at a time.
    
    gray_image = grayscale(original)   
    for x, y, col in gray_image: # col is the Color object for the pixel @ (x,y)
                                 # There's no need to unpack that object into
                                 # RGB components.
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

# poor_test_grayscale1()
# poor_test_grayscale2()
test_grayscale()