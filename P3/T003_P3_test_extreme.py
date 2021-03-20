#Author: Jacob Ridgway
#Student ID: 101195221
#Group No.: T003
#----------------------------------------------------------------------
from Cimpl import *
from .T003_P3_filter_extreme import extreme_contrast
from unit_testing import check_equal
#----------------------------------------------------------------------
def test_extreme() -> None:
    """
    Test function for extreme contrast filter.
    
    >>> test_extreme
    """

    original = create_image(3,1)
    set_color = (original, 0,0, (160,230,40))
    set_color = (original, 1,0, (225,10,130))
    set_color = (original, 2,0, (20,100,255))
    
    expected = create_image(3,1)
    set_color = (expected, 0,0, (255,255,0))
    set_color = (expected, 1,0, (225,0,255))
    set_color = (expected, 2,0, (0,0,255))
    
    actual_filtered_image = extreme_contrast(original)
    
    for x,y, col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
#-----------------------------------------------------------------------
#Main Script        
if __name__ == "__main__":
    file = choose_file()
    image = load_image(file)
    extreme_image = extreme_contrast(image)
    show(extreme_image)
    
    test_extreme()
    
    
    
    
