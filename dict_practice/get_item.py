def get_items(d):
    items=[]
    for key in d:
        items.append((key,d[key]))
    return items
d = {
    "name": "Komal",
    "age": 22,
    "course": "Python"
}

result = get_items(d)
print("items:", result)
