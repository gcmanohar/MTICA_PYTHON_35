class Dog:
    price=500   #class aatibute ,created by assigning variables within
                     # tha body of class.
    def __init__  (self,name,color):
        self.name=name
        self.color=color

    def bark(self):           # it will write overal object
        print('woof')
        print(self.name , " has" ,self.price, "price and its color is ", self.color)
if __name__=="__main__":
    pet1=Dog('Chintu','wight')     #object creation with class name
    pet2=Dog('Charly','red')
    pet1.bark()
    pet2.bark()

    print(pet2.price)
    print(pet2.price)
    print(Dog.price)
    Dog('abc','black').bark()
