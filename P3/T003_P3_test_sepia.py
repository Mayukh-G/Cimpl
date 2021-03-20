"""
Author: Alex Watson
Group: T003
StudentNum: 101178559
"""
from Cimpl import *
from T003_P3_filter_sepia import sepia_filter
from unit_testing import check_equal



def test_sepia() -> None:
    """
    A test function for sepia. 
    
    >>>test_sepia()
    
    """
    original = create_image(3, 1) #Creating an original image to be tested  by the sepia filter.
    set_color(original, 0, 0,  create_color(45, 67, 233))
    set_color(original, 1, 0,  create_color(120, 27, 38))
    set_color(original, 2, 0,  create_color(255, 37, 54))    
    
    expected1 = create_image(3, 1)
    set_color(original, 0, 0,  create_color(132, 115, 97)) #Medium gray
    set_color(original, 1, 0,  create_color(67, 61, 54)) #Light gray
    set_color(original, 2, 0,  create_color(232, 215, 199))  #Dark gray 
    
    sepia_test = sepia_filter(original)
    for x, y, col in sepia_test:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected1, x, y))
        
#Main Script
test_sepia()
    
    
