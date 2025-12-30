''' Question = Write a program to rotate a list to the left by k positions without 
    using slicing or built-in functions.'''
    
from list_length import list_length
def rotate_left(lst, k=2):
    n = list_length(lst)
    rotated = []

    for i in range(k, n):
        rotated.append(lst[i])

    for i in range(k):
        rotated.append(lst[i])

    print("Rotated List:", rotated)
    return rotated
lst = [1, 2, 3, 4, 5]
rotate_left(lst)