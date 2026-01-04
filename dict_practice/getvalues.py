def get_value(d):
    values=[]
    for key in d:
        values.append(d[key])
    return values
d = {
    "name": "Komal",
    "age": 22,
    "course": "Python"
}

result = get_value(d)
print("Values:", result)
