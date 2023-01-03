import math as m
class Circle:
    pi=22/7
    def __init__(self,r):
        self.r=r
       
    def CalculatArea(self):
        t= self.pi*self.r**2
        return t
    def CalculatParameter(self):
        t= 2*self.pi*self.r
        return t

r=int(input())
ob=Circle(r)
area=ob.CalculatArea()
para=ob.CalculatParameter()
print(area)
print(para)
