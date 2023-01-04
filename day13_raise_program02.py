#raise an error and stop tha porgram if x is no in integer---
#x='hello'
x=input()
if not type(x) is int:
    raise TypeError ("Only integers alowed")
