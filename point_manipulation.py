# Useful functions for the draw_curve function and its accompanying functions

# get_x_y_lists converts points stored as a list of tuples, to a list containing a
# list of the x coordinates and a list of the y coordinates
# Note that the coordinate lists are needed by function polyfit
def get_x_y_lists(points: list) -> list:
    """
    Returns a list containing two lists: the x coordinates, and the y
    coordinates given a list of point tuples.

    >>> get_x_y_lists([(1,4),(2,3)])
    [ [1,2], [4,3] ]
    >>> get_x_y_lists([(1,1),(2,2),(3,3)])
    [ [1,1,1], [2,2,2] ]
    >>> get_x_y_lists([(0,10),(20,37),(99,120),(200,0)])
    [ [0,20,99,200], [10,37,120,0] ]
    """
    xlist = []
    ylist = []
    for (x, y) in points:
        xlist += [x]
        ylist += [y]
    return [xlist, ylist]


# _take_first takes the first element for sort (used to sort the points entered and the
# border points returned), see sort() and sorted() "key=", e.g. here:
# https://www.programiz.com/python-programming/methods/list/sort
def _take_first(elem: tuple) -> int:
    """
    Returns the first element of a tuple of ints.

    >>> _take_first( (1,2) )
    1
    >>> _take_first( (2,1) )
    2
    >>> _take_first( (1,1) )
    1
    """
    return elem[0]


# sort_points is used to sort a list of point tuples
def sort_points(points: list) -> list:
    """
    Returns a list of point tuples equivalent to points, but sorted in order
    by ascending x coordinate.

    >>> sort_points([(5,4),(2,3)])
    [(2,3),(5,4)]
    >>> sort_points([(1,1),(3,2),(2,3)])
    [(1,1),(2,3),(3,2)]
    >>> sort_points([(99,120),(0,10),(200,0),(20,37)])
    [(0,10),(20,37),(99,120),(200,0)]
    """
    return sorted(points, key=_take_first)
