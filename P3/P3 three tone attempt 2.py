'''
Author : Alexander Christie
StudentNum : 101185138
Group : T003
'''

from Cimpl import *
# I will import specific functions once I have figured out exactly what I need 
BLACK = ('black', 0, 0, 0) 
WHITE = ('white', 255, 255, 255)
BLOOD = ('blood', 255, 0, 0)
GREEN = ('green', 0, 255, 0)
BLUE = ('blue', 0, 0, 255)
LEMON = ('lemon', 255, 255, 0)
AQUA = ('aqua', 0, 255, 255)
PINK = ('pink', 255, 0, 255)
GRAY = ('gray', 128, 128, 128)
colours = [BLACK, WHITE, BLOOD, GREEN, BLUE, LEMON, AQUA, PINK, GRAY] 

def three_tone(colour1: str, colour2: str, colour3: str, image: Image) -> Image:
    # The Parameters are strings, but the arguments you pass in are Tuples. The function definition requires the colours
    # to be passed in as strings
    '''
    Returns a copie of the input image filtered with all pixles with average 
    brightness in range 0-84 as colour defined by colour1, similarly pixles with
    brighness in range 85-170 the pixles have colour defined by the argument 
    colour2. Finally, pixles with average brighness in range 171-255 will be 
    assigned the colour defined by colour3. 
     
    >>> image = load_image(choose_file())
    >>>show(image)
    >>> three_tone_image = three_tone(black, white, blue, image)
    >>>show(three_tone_image)
    '''
    
    duplicate = copy(image)
    for pixel in duplicate:
        x, y, (r, g, b) = pixel
        brightness = round((r + g + b) / 3)

        if brightness <= 84:
            i = 0
            for i in range(len(colours)):
                if colours[i][0] == colour1:
                    color, r, g, b = colours [i]
                    new_colour = create_color (r, g, b)
                i += 1
            

        elif 85 <= brightness <= 170:
            i = 0
            for i in range(len(colours)):
                if colours[i][0] == colour2:
                    color, r, g, b = colours [i]
                    new_colour = create_color (r, g, b)
                i += 1            
        

        else:
            i = 0
            for i in range(len(colours)):
                if colours[i][0] == colour3:
                    color, r, g, b = colours [i]
                    new_colour = create_color (r, g, b)      
            
        set_color(duplicate, x, y, new_colour)

    return duplicate


if __name__ == '__main__':
    # I added this line to the main script so that it wont run when I import it into the test function
    # I also reformatted things so that they follow PEP8 conventions, basically spaces after commas, whitespaces around
    # operators ect.
    image = load_image(choose_file())
    x = three_tone('blue', 'black', 'blood', image)
    show(x)

'''
Proposed test cases 
- pixels in each range
- pixels on boundary values, (0,0,0),(255,255,255),(84,84,84)
- pixels with avg brightness as a float 
- argument 3 tone colors are all the same
- when an image with no pixels is loads 
'''