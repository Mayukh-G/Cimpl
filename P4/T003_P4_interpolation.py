# Author: Jacob Ridgway
# Student ID: 101195221
# Group NO.: T003
#-----------------------------------------------------------------------
import math
import numpy
#-----------------------------------------------------------------------
def _interpolation(points: list) -> list:
    """
    Returns coefficients of interpolating polynomial as a list, and coefficients of the 
    quadratic regression polynomial (if user entered more than 3 points).
    
    >>> 
    >>>
    """

    if len(points_list) <= 2:
        degree = 1
    else:
        degree = 2
    x_point, y_point = points
    
    return numpy.polyfit(x_point, y_point, degree)

#-------------------------------------------------------------------------
points_list = [(1,2), (3,4)]

print(_interpolation(points_list))