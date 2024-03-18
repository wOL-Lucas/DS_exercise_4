import numpy as np


def get_list_items(list_max_length:int, dtype=int):
    for i in range(list_max_length):
        yield dtype(input(f"Enter the {i+1}º number: "))
    
