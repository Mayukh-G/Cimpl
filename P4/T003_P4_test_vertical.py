'''
Author : Alexander Christie
Student : 101185138
Group: T003
'''
from T003_P4_filter_vertical import flip_vertical
from Cimpl import *
from unit_testing import check_equal


def test_vertical_flip()-> None: 
    '''
    tests that the pixls change positions properly in the vertical_flip filter.
    >>> test_posterize()
    '''
    original = create_image(3, 3)
    set_color(original, 0, 0, create_color(1, 1, 1))
    set_color(original, 1, 0, create_color(255,0,3))
    set_color(original, 2, 0, create_color(0,0,0))
    set_color(original, 0, 1, create_color(255,255,255))
    set_color(original, 1, 1, create_color(31,95,159))
    set_color(original, 2, 1, create_color(65,233,111))
    set_color(original, 0, 2, create_color(0,0,0))
    set_color(original, 1, 2, create_color(10,10,10))
    set_color(original, 2, 2, create_color(31,31,31))
    expected = create_image(3, 3)
    set_color(expected, 0, 0, create_color(0, 0,0))
    set_color(expected, 1, 0, create_color(10, 10, 10))
    set_color(expected, 2, 0, create_color(31, 31, 31))
    set_color(expected, 0, 1, create_color(255, 255, 255))
    set_color(expected, 1, 1, create_color(31, 95, 159)) 
    set_color(expected, 2, 1, create_color(65, 233, 111))
    set_color(expected, 0, 2, create_color(1,1,1))
    set_color(expected, 1, 2, create_color(255,0,3))
    set_color(expected, 2, 2, create_color(0,0,0))    
        
    fliped_image = flip_vertical(original)
    
    for x, y, col in fliped_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))  

# Main Script 
if __name__ == '__main__':
    test_vertical_flip()
