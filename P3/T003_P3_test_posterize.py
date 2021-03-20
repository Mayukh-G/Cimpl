'''
Author : Alexander Christie
StudentNum : 101185138
Group : T003
'''
from T003_P3_filter_posterize import _adjust_component, posterize_filter
from Cimpl import *
from unit_testing import check_equal

def test_posterize()-> None: 
    '''
    tests the posterize filter function
    >>> test_posterize()
    '''
    original = create_image(3, 2)
    set_color(original, 0, 0, create_color(64,64,64))
    set_color(original, 1, 0, create_color(191,191,191))
    set_color(original, 2, 0, create_color(0,0,0))
    set_color(original, 0, 1, create_color(255,255,255))
    set_color(original, 1, 1, create_color(31,95,159))
    set_color(original, 2, 1, create_color(65,233,111))
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

# Main Script 
if __name__ == '__main__':
    test_posterize()
    
    
    