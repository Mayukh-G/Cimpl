'''
Author : Alexander Christie, Alex Watson
Student : 101185138, 101178559
Group: T003

from Cimpl import *
from T003_image_filters import *


#Functions used in the UI 4
command= input(" L)oad image    S)ave-as \n \
3)-tone    X)treme contrast    T)int sepia    P)osterize \n \
E)dge detect    D)raw curve    V)ertical filp    H)orizontal flip \n \
Q)uit \n \n : ")

           
def detect_edges_ui (image: Image) -> Image:
    '''
    Takes the image from the UI and prompts the user to give the additional 
    threshold value
    >>>
    >>> Need to add examples 
    >>>
    '''
    threshold = float(input("input threshold value: "))
    image = detect_edges(image, threshold)
    return image
    
def draw_curve_ui (image: Image) -> Image:
    '''
    Takes the image from the UI and propmts the user to provide the additional 
    nessary information to run the draw curve function, the color of the line 
    must be added along with the coordinates.
    >>>
    >>>  Need to add examples 
    >>>
    '''
    col = input("input the color of the line ")
    coords = []
    x = input("input the x coordinate of the desired point or stop to stop inputing points  ")
    while x != 'stop':
        y = input("input the y coordinate of the desired point ")
        y = int(y)
        x = int(x)
        tup = (x,y)
        coords += [tup]
        x = input("input the x coordinate of the desired point or stop to stop inputing points  ")
    return draw_curve(image, col, coords)
    
# all values in command dict are functions, once coded for their quotations should be removed
command_dict = {'L': 'load_image', 'S': 'save_as', '3': 'three_tone', 
               'X': 'extreme_contrast', 'T': 'sepia_filter', 'P': 'posterize_filter',
               'E': detect_edges_ui, 'D': draw_curve_ui, 'V':flip_vertical,
               'H': flip_horizontal, 'Q': 'quit'}
   
 
#Main UI
image = load_image(choose_file()) #This line should be removed once the load_image function is added 
command = str.capitalize(command)
while command != 'Q':
    command = str.capitalize(command)
    if command_dict.get(command) != None:
        if type(image) == Image:
            image = command_dict.get(command)(image)
            show(image)
        else: 
            print("No image loaded")
    else:
        print("No such command")
    
    command= input(" L)oad image    S)ave-as \n \
    3)-tone    X)treme contrast    T)int sepia    P)osterize \n \
    E)dge detect    D)raw curve    V)ertical filp    H)orizontal flip \n \
    Q)uit \n \n : ")    
    command = str.capitalize(command)
