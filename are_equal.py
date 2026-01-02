def are_equal(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


a =[1,2,4,6,8]
b = [1,2,4,6,8]

print(are_equal(a, b))
