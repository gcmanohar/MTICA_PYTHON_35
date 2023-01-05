class BaseMain:
    price=500
    def __init__(self, name,color):
        self.name=name
        self.color=color
    def bark_main(self):
        print("gir.................")
class Dog_deriv(BaseMain):
    def bark_derived(self):
        print('wooff')
if __name__ == "__main__":
    p1=Dog_deriv('tomy','red')
    p1.bark_main()
    p1.bark_derived()
    print(p1.name , ' is of color ' ,p1.color, 'with price is ',BaseMain.price)
    
    
