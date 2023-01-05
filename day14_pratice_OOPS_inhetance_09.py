# operator overloading
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,ob):
        return Vector2D(self.x + ob.x , self.y + ob.y)
    def __sub__(self,other):
        return Vector2D(self.x - other.x , self.y - other.y)

first=Vector2D(5,7)
second=Vector2D(5,9)
res=first + second
print(res.x)
print(res.y)
res=first - second
print(res.x)
print(res.y)
