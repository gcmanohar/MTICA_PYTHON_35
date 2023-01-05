class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name , "destroyed")

pt1=Point()
pt2=Point(5,7)
pt3=pt2
pt4=pt3
print(id(pt2),id(pt3),id(pt4))

del pt2
del pt3
del pt4
pt2=Point(1,2)
print(pt2)
