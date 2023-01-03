
class Number:
    def __init__(self,n):
        self.n=n
    def AmstramCheck(self):
       # assert (n<=0 ), "INVALID"
        self.n=str(self.n)
        tot=0
        for i in self.n:
            tot+=int(i)**len(self.n)
        if int(self.n)==tot:
            return "Amstramg"
        else:
            return "not Amstramg"
n=input()
ob=Number(n)

 print(ob.AmstramCheck())
    
