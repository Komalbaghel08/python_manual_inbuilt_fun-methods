def key_exists(d,target):
    for i in d:
        if i == target:
            return True
    return False
d = {
    "name": "Komal",
    "age": 22,
    "course": "Python"
}
target = "namee"
r = key_exists(d,target)
print("key_exists",r)