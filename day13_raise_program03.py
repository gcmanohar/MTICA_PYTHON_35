#raise an error and stop tha porgram if x divisable by zero---
a=int(input())
b=int(input())
try:
    if a<0 or b<0:
        raise Exception
    print(a/b)
except Exception as e:
    print("place enter valid integer")
