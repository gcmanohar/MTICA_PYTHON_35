class Cat:
    def __init__  (self,color,legs):
        self.color=color
        self.legs=legs

    def __str__(self):     # it will write overal object
        return 'cat is ' + self.color+ 'color ' +'and has ' + str(self.legs) +' legs '
if __name__=="__main__":
    pet1=Cat('black',4)     #object creation with class name
    pet2=Cat('red',3)
    print(pet1.color)
    print(pet1.legs)
    print(pet1)

    print(pet2.color)
    print(pet2.legs)
    print(pet2)
