class Animal:
    price=500
    def __init__(self, name,color):
        self.name=name
        self.color=color
##    def bark_main(self):
##        print("gir.................")
class Cat(Animal):
    def mew(self):
        print('Cat memos')
class Dog(Animal):
    def bark(self):
        print("dog momes")
        
if __name__ == "__main__":
    print(__name__)
    p1=Dog('tomy','red')
    p2=Cat('blacky','wight')
    p1.bark()
    p2.mew()
    print(p1.name)
    print(p2.name)
    
