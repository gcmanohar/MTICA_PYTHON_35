#variable lengrh
def add(*n):
    t=0
    for i in n:
        t+=i
    return t
print("add():",add())
print("add(5):",add(5))
print("add(5,7):",add(5,7))
print("add(7,45,32,0):",add(7,45,32,0))
print("add(7,7,11,5,77,33):",add(7,7,11,5,77,33))

