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


 
numbers = random_list() # not ordered list
print(f"This is unordered list: {numbers}")
new_numbers = quicksort(numbers)
print(f"This is ordered list: {new_numbers}")
