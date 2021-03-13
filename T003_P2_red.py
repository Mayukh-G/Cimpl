'''
Author: Alexander Christie
StudentNum: 101185138
Group: T003
'''
from Cimpl import *
from unit_testing import check_equal

def red_channel(image: Image) -> Image:
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
        x, y, (r,g,b) = pixle
        new_color = create_color(r,0,0) 
        set_color (duplicate, x,y,new_color)    
    return duplicate

def test_red_channel() ->None:
    '''
    Test the red_channel function using the check_equal function
    '''
    original = create_image(3, 2)
    set_color(original, 0, 0, create_color(125,125,125))
    set_color(original, 1, 0, create_color(255,255,255))
    set_color(original, 2, 0, create_color(0,0,0))
    set_color(original, 0, 1, create_color(75,13,150))
    set_color(original, 1, 1, create_color(245,19,0))
    set_color(original, 2, 1, create_color(90,0,16))
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

# Main Script 
if __name__ == '__main__':   
    file = choose_file()
    image = load_image(file)
    red_image = red_channel(image)
    show(image)
    show(red_image)
    test_red_channel()