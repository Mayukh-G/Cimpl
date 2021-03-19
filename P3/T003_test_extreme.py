#Author: Jacob Ridgway
#Student ID: 101195221
#Group No.: T003
#----------------------------------------------------------------------
import Cimpl *
from T003_P3_extreme import extreme_contrast

def test_extreme(image: Image) -> str:
    """
    Test function for extreme contrast filter.
    
    >>> test_extreme
    """

    original = create_image(3,1)
    set_color = (test_image, 0,0, (160,230,40))
    set_color = (test_image, 1,0, (225,10,130))
    set_color = (test_image, 2,0, (20,100,255))
    
    filtered_image = (extreme_contrast(original))
    
    
    
    