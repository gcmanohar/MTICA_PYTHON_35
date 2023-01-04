def cubeNo():
    i=1
    while True:
        yield i*i*i
        i=i+1
##y_List=[i for i in squares()]
##print(y_List)
for i in cubeNo():
    if i > 1000:
        break
    print(i)
