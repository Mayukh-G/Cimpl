# Milestone 3
# Submitted : 08/04/2021
# Group  : T003
# Course : ECOR1042G
# Number : 101195221, 101181018
# Names  : Jacob Ridgway, Mayukh Gautam
from typing import List, Tuple
from T003_image_filters import *


# J : 3, X, T, P
# M : E , V, H


def _get_args() -> List[List[str]]:  # Mayukh Gautam
    """
    Promts user for the batch filename
    Gathers commands from a txt file acting as a batch file
    Splits up commands into a list and returns the list

    >>> _get_args()
    [["example.png", "save_to.png", "X", "3"], ["example2.png", "save_to2.png", "D", "H", "V"]]
    :return:
    """
    user_in = input("Enter batch file path (excluded extension will result in .txt being assumed):\n")
    if "." not in user_in:
        user_in += ".txt"
    batch_file = open(user_in)
    args = []
    for line in batch_file:
        args.append(line.split())
    return args


def _parse_args(unparsed: List[List[str]]) -> List[dict]:  # Jacob Ridgway
    """
    Return a list of dictionaries. Each dictionary corresponds to one line in the batch file
    {"Image": fn (Image), "Save": sv (str), "Filters": list ("str")}
    """
    
    main_list = []
    
    for lines in unparsed:
        parsed = dict()
        file = lines
        img = Image(file[0])  # make an image type
        save = file[1]
        filters = file[2:]
        parsed.update({"Image": img, "Save": save, "Filters": filters})
        main_list.append(parsed)
            
    return main_list


function_map = {"E": detect_edges, "V": flip_vertical, "H": flip_horizontal, "3": three_tone, "X": extreme_contrast,
                "T": sepia_filter, "P": posterize_filter}


def modify() -> None:  # Mayukh Gautam, Jacob Ridgway
    # Gathering information
    commands = _parse_args(_get_args())
    # Executing filters
    for command in commands:
        img = command["Image"]
        for filter_arg in command["Filters"]:
            if filter_arg == "3":
                img = function_map[filter_arg]("aqua", "blood", "lemon", img)
            elif filter_arg == "E":
                img = function_map[filter_arg](img, 15)
            else:
                img = function_map[filter_arg](img)
        save_as(img, command["Save"])  # Save image to user inputted location


if __name__ == '__main__':
    # modify will act as the main function. It will call all other functions
    modify()
