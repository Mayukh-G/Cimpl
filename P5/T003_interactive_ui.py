'''
Author : Alexander Christie, Alex Watson
Student : 101185138, xxxx
Group: T003
'''
from T003_image_filters import *

# This part of the UI contains E) D) V) H) Q) 

#Functions used in the UI 4
comand= input(" L)oad image    S)ave-as \n \
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
    threshold = input("input threshold value: ")
    image = detect_edges(image, threshold)
    
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
    

comand_dict = {'L': load_image, 'S': save_as, '3': three_tone, 
               'X': extreme_contrast, 'T': sepia_filter, 'P': posterize_filter,
               'E': detect_edges, 'D': _image_border_finding, 'V':flip_vertical,
               'H': flip_horizontal, 'Q': quit}
               
               

# Main UI
while comand != Q or comand !=q:
    comand = str.capitalize(comand)
    if comand_dict.get(comand) != None:
        if type(image) == Image:
            image = comand_dict.get(comand)(image)
            
        else: 
            print("No image loaded")
    else:
        print("No such command")
    
    comand= input(" L)oad image    S)ave-as \n \
    3)-tone    X)treme contrast    T)int sepia    P)osterize \n \
    E)dge detect    D)raw curve    V)ertical filp    H)orizontal flip \n \
    Q)uit \n \n : ")    
