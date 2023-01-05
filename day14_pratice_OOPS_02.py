class Dog:
    price=500
    def __init__(self,color,name):
        self.color=color
        self.name=name
    def bark(self):
        print("dog is " + self.color +" color"+ " and whose name is "
        +self.name+ " and its price is " +str(self.price))
        return
if __name__=="__main__":
    col=input()
    name=input()
    p1=Dog(col,name)
    p2=Dog(col,name)
    p1.bark()
    p2.bark()
    print(p1.color)
    print(p1.name)
    print(Dog.price)
    Dog('blue','juju').bark()
  
