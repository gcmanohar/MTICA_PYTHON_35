#method overriding
class Animal:
    price=500
    def __init__(self, name,color):
        self.name=name
        self.color=color

    def bark(self):
        print("gir.................")
class Cat(Animal):
    def bark(self):
        print('Overriding')
        
if __name__ == "__main__":
    print(__name__)
    p1=Animal('juju','black')
    p2=Cat('blacky','wight')
    p1.bark()
    p2.bark()
    print(p1.name)
    print(p2.name)
    Cat('abc','xyz').bark()
    
