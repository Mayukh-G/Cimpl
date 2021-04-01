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
