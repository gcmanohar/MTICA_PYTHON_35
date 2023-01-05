# operator overloading
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,ob):
        temp= self.real + ob.real , self.imag + ob.imag
        return temp
    def __sub__(self,ob):
        temp= self.real - ob.real , self.imag - ob.imag
        return temp
    def __mul__(self,ob):
        temp= (self.real * ob.real - self.imag * ob.imag,
               self.real * ob.imag + self.imag * ob.real)
        return temp
    
    def __str__(self):
        return (self.rear,self.imag)

ob1=Complex(3,5)
ob2=Complex(5,7)
#ob3=ob1.add(ob2) 'Complex' object has no attribute 'add'
ob4=ob1 + ob2
ob5=ob1 - ob2
ob6=ob1*ob2
print(ob4)
print(ob5)
print(ob6)
##print(ob4.real): 'tuple' object has no attribute 'real'
##print(ob4.imag)
