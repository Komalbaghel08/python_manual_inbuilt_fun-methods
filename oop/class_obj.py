class Demo:
    pass
a = Demo
b = Demo()
print("Adrs of class (without parenthesis):", id(a))
print("Adrs of object (with parenthesis):", id(b))
print(dir(Demo))