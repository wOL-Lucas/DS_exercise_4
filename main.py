import numpy as np
from utils import Input

class NonOrderedList:
    def __init__(self, max_length:int) -> None:
        self.__last_position__ = 0
        self.__elements__ = np.empty(max_length, dtype=int)
    
    def push(self, element:int):
        if self.__last_position__ == len(self.__elements__):
            self.__RaiseFullListError()

        if self._is_duplicate(element):
            self.__RaiseDuplicateError()

        self.__elements__[self.__last_position__] = element
        self.__last_position__ += 1

    def pop(self):
        self.__last_position__ -= 1
        return self.__elements__[self.__last_position__]

    def __iter__(self):
        for i in range(self.__last_position__):
            yield self.__elements__[i]
    
    def __str__(self):
        return str([item for item in self])

    def _is_duplicate(self, element:int):
        for index,item in enumerate(self.__elements__):
            if item == element and index < self.__last_position__:
                return True
            
        return False


    def __RaiseDuplicateError(self):
        raise Exception("Duplicate item error","The list does not accept duplicate items")
    
    def __RaiseFullListError(self):
        raise Exception("List full error","The list is full")

max_length = 10
nonOrderedList = NonOrderedList(max_length)

for item in Input.get_list_items(max_length, dtype=int):
    nonOrderedList.push(item)

print("NonOrderedList: ", nonOrderedList)

