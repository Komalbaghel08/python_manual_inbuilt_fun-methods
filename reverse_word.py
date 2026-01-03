def reverse(l):
    rev=""
    for i in l:
        rev = [i]+rev
    return rev
l = [1,2,34]
print(reverse(l))
