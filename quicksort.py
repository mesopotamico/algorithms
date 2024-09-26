from binary_search import random_list

def quicksort(numbers):
    length = len(numbers)

    if length <= 1:
        return numbers 

    pivot = numbers.pop()
    greater = []
    lower = []
    
    for i in numbers:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)

    return quicksort(lower) + [pivot] + quicksort(greater)

