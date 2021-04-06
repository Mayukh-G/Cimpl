'''
Author : Alexander Christie, Alex Watson
Student : 101185138, 101178559
Group: T003
'''

from Cimpl import *
from T003_image_filters import *
import sys

#Functions used in the UI 4

command = input(" L)oad image    S)ave-as \n \
3)-tone    X)treme contrast    T)int sepia    P)osterize \n \
E)dge detect    D)raw curve    V)ertical filp    H)orizontal flip \n \
Q)uit \n \n : ")



def load_image_ui (image: Image) -> Image: 
    '''
    Loads the user's desired image
    >>>
    >>> Need Examples
    >>>
    '''
    image = load_image(choose_file())
    return image

def save_as_ui (image: Image) -> None :
    '''
    Saves the users image. 
    >>>
    >>>Need Examples
    >>>
    '''
    save_as(image)
    
def three_tone_ui (image: Image) -> Image:
    '''
    Takes the image from the ui and applie a three tone filter. 
    >>>
    >>>Need Examples
    >>>
    '''
    image = three_tone('cyan', 'blood', 'lemon', image)
    return image

def extreme_ui (image: Image) -> Image:
    '''
    Takes and image from the ui and applies an extreme contrast filter
    >>>
    >>>Need Examples
    >>>
    '''
    image = extreme_contrast(image)
    return image

def sepia_ui (image: Image) -> Image:
    '''
    Takes and image from the ui and applies a sepia filter. 
    >>>
    >>>Need Examples
    >>>
    '''
    image = sepia_filter(image)
    return image

def posterize_ui(image: Image) -> Image:
    '''
    Takes an image from the user and applies a posterizing filter. 
    >>>
    >>>Need Examples
    >>>
    '''
    image = posterize_filter(image)
    return image
    

def detect_edges_ui (image: Image) -> Image:
    '''
    Takes the image from the UI and prompts the user to give the additional 
    threshold value
    >>> : L
    >>> : E
    >>> input threshold value: 10
    '''
    threshold = float(input("input threshold value: "))
    image = detect_edges(image, threshold)
    return image
    
def draw_curve_ui (image: Image) -> Image:
    '''
    Takes the image from the UI and propmts the user to provide the additional 
    nessary information to run the draw curve function, the color of the line 
    must be added along with the coordinates.
    >>> : l
    >>> : d
    >>> How many coordinates would you like to input?
    >>> 2
    >>>Enter coordinate n.1. With this format: x,y 
    >>> 1,1
    >>>Enter coordinate n.2. With this format: x,y
    >>> 300,300
    '''
    col = "lemon"
    
    return draw_curve(image, col)[0]
    
command_dict = {'L': load_image_ui, 'S': save_as_ui, '3': three_tone_ui, 
               'X': extreme_ui, 'T': sepia_ui, 'P': posterize_ui,
               'E': detect_edges_ui, 'D': draw_curve_ui, 'V':flip_vertical,
               'H': flip_horizontal, 'Q': 'quit'}
   
 
#Main UI
command = str.capitalize(command)
while command != 'Q':
    command = str.capitalize(command)
    if command_dict.get(command) != None:
        if command =='L':
            image = load_image(choose_file())
        elif type(image) == Image:
            image = command_dict.get(command)(image)
            show(image)
        else: 
            print("No image loaded")
    else:
        print("No such command")
    
    command = input(" L)oad image    S)ave-as \n \
    3)-tone    X)treme contrast    T)int sepia    P)osterize \n \
    E)dge detect    D)raw curve    V)ertical filp    H)orizontal flip \n \
    Q)uit \n \n : ")    
    command = str.capitalize(command)
