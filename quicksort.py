from binary_search import random_list
import numpy as np
import time


def quicksort(vector):
    
    if  len(vector) != 0: 
        end = len(vector) - 1 
    else:
        end = len(vector)

    start = 0
    if start < end:
        right_pos = locate_pivot(vector, start, end)

        quicksort(vector[:right_pos-1])
        quicksort(vector[right_pos+1:])





def locate_pivot(vector, start, end):
    while start < end:
        while vector[end] >= vector[start] and start < end:
            end -= 1
            print(f"pivote derecha {start} {end}")
            #time.sleep(0.1)

        vector[start], vector[end] = vector[end], vector[start]

        while vector[start] <= vector[end] and start < end:
            start += 1
            print(f"pivote izquierda: {start} {end}")
            #time.sleep(0.1)
        vector[start], vector[end] = vector[end], vector[start]
    return start



numbers = random_list() # not ordered list
numbers = np.array(numbers)
print(f"Nor ordered list: {numbers}")
quicksort(numbers)
print(f"Ordered list: {numbers}")
