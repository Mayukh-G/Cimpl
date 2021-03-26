# Author: Jacob Ridgway
# Student ID: 101195221
# Group NO.: T003
#----------------------------------------------------------------
from Cimpl import *
from T003_P4_filter_edge import detect_edges
from unit_testing import check_equal
#----------------------------------------------------------------
def test_edge_detection() -> str:
    '''
    Tests edge detection function.
    '''
    
    original = create_image(3,3)    
    set_color(original, 0,0,create_color(60,78,120)) #First row, xpos 1
    set_color(original, 1,0,create_color(82,55,210)) #xpos 2
    set_color(original, 2,0,create_color(45,56,34))  #xpos 3
    
    set_color(original, 0,1,create_color(60,78,120)) #Second row, xpos 1
    set_color(original, 1,1,create_color(67,23,230)) #xpos 2
    set_color(original, 2,1,create_color(45,56,34))  #xpos 3
    
    set_color(original, 0,2,create_color(23,255,130)) #These are on the bottom of the image
    set_color(original, 1,2,create_color(56,234,210))
    set_color(original, 2,2,create_color(55,45,120))
    
    
    expected = create_image(3,3)
    set_color(expected, 0,0,create_color(255,255,255)) #First row, xpos 1, Using threshold of 1
    set_color(expected, 1,0,create_color(0,0,0)) #xpos 2
    set_color(expected, 2,0,create_color(255,255,255)) #xpos 3
    
    set_color(expected, 0,1,create_color(0,0,0)) #Second row, xpos 1
    set_color(expected, 1,1,create_color(0,0,0)) #xpos 2
    set_color(expected, 2,1,create_color(0,0,0)) #xpos 3 
    
    set_color(expected, 0,2,create_color(255,255,255)) #Bottom pixels get set to white
    set_color(expected, 1,2,create_color(255,255,255))
    set_color(expected, 2,2,create_color(255,255,255))

    
    actual_filtered_image = detect_edges(original,1)
    
    for x,y, col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))
#------------------------------------------------------------------------------
# Main Script
if __name__ == "__main__":  
    test_edge_detection()