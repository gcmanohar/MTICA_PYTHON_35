class Cat:
    def __init__(self,color,leg):
        self.color=color
        self.leg=leg
    def __str__(self):
        temp="cat is" + self.color +" color"+ "and it have "+ str(self.leg)+ " legs"
        return temp
if __name__=="__main__":
    col=input()
    ln=int(input())
    p1=Cat(col,ln)
    p2=Cat(col,ln)
    print(p1.color)
    print(p1.leg)
    print(p1)
