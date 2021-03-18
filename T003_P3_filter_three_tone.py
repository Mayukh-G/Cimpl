'''
Author : Alexander Christie
StudentNum : 101185138
Group : T003

'''

from Cimpl import * 

BLACK = (0,0,0)
WHITE = (255,255,255)
BLOOD = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LEMON = (255,255,0)
AQUA = (0,255,255)
PINK = (255,0,255)
GRAY = (128,128,128)

def three_tone(colour1: str, colour2: str, colour3: str, image: Image)-> Image:
    '''
    Returns a copie of the input image filtered with all pixles with average 
    brightness in range 0-84 as colour defined by colour1, similarly pixles with
    brighness in range 85-170 the pixles have colour defined by the argument 
    colour2. Finally, pixles with average brighness in range 171-255 will be 
    assigned the colour defined by colour3. 
     
    >>> image = load_image(choose_file())
    >>>show(image)
    >>> three_tone_image = three_tone(black,white,blue,image)
    >>>show(three_tone_image)
    '''
    duplicate = copy(image)
    for pixle in duplicate:
        x, y, (r,g,b) = pixle
        brightness = round((r+g+b)/3)
        
        if brightness <= 84:
            (r,g,b) = colour1
            new_colour = create_color(r,g,b)
        
        if 85<=brightness<= 170:
            (r,g,b) = colour2
            new_colour = create_color(r,g,b)
        
        else:
            (r,g,b) = colour3
            new_colour = create_color(r,g,b) 
            
        set_color (duplicate, x,y,new_colour)   
        
    return duplicate 

image = load_image(choose_file())
x = three_tone(BLACK,BLUE,WHITE,image)
show(x)

'''
Proposed test cases 
- pixles in each range
- pixls on boundry values, (0,0,0),(255,255,255),(84,84,84)
- pixls with avg brighness as a float 
- argument 3 tone colors are all the same
- when an image with no pixles is loads 
'''
