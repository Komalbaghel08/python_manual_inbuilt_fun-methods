''' Question = Write a program to rotate a list to the left by k positions without 
    using slicing or built-in functions.'''
    
def rotate_left(lst, k):
    n = len(lst)
    rotated = []

    for i in range(k, n):
        rotated.append(lst[i])

    for i in range(k):
        rotated.append(lst[i])

    return rotated


n = 5
lst = [1,5,2,3,10]
k = 2

print(rotate_left(lst, k))


'''OR'''
lst = list(map(int, input().split()))
k = int(input())
print(rotate_left(lst, k))