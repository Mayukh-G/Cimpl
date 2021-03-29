"""
Author: Alex Watson
SutdentNum: 101178559
Group: T003
"""
from Cimpl import *
from unit_testing import check_equal
from T003_P4_filter_draw import *


def test_draw() -> None:
    """
    Tests the draw filter. 
    
    >>>test_draw()
    """

    original = create_image(20, 20)  # creating a blank 20x20 image
    test_curve = draw_curve(original, "blue", [(0, 0), (10, 10), (20, 20)])

    expected = create_image(20, 20)  # creates a blank image for expected
    for i in range(20):
        set_color(expected, i, i, create_color(0, 0, 255))  # sets diagonal line downwards in expected
        for j in range(i - 4, i + 5):  # adds coloured pixels +/- 4 from line
            if j in range(20):  # ensures they do not draw out of image
                set_color(expected, i, j, create_color(0, 0, 255))
    for x, y, col in test_curve[0]:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))
        
        
    #Testing Return Points
    expected_return_points = [(0,0), (20,20)]
    if expected_return_points == test_curve[1]:
        result = "PASSED"
    else:
        result = "FAILED"
    print("Checking return points: ", result)
    print("Expected: ", expected_return_points, ", got: ", test_curve[1])
        


# Main Script:
if __name__ == '__main__':
    test_draw()
    
