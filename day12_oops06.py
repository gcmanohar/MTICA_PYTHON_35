
class Rectangle:
   
    def __init__(self,l,w):
        assert (l>=0 and w>=0), "INVALID"
        self.l=l
        self.w=w
       
    def CalculatArea(self):
        
        t= self.l*self.w         #l*w

        return t
    def CalculatePerimeter(self):
        t=2*(self.l+self.w)   #2*(l+w)
        return t

l=int(input())
w=int(input())
try:
    ob=Rectangle(l,w)
    area=ob.CalculatArea()
    pera=ob.CalculatePerimeter()
    print(area)
    print(pera)

except AssertionError as o:
    print(o)
  
