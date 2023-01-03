
class Number:
    def __init__(self,n):
        self.n=n
    def primeCheck(self):
        assert (n>=0), "INVALID"
        if (self.n==1 or self.n==2 or self.n==3):
            return self.n
        for i in range(2,self.n):
            if self.n%i==0:
                return "not prime"
        return " prime"
n=int(input())
try:
    ob=Number(n)
    print(ob.primeCheck())
except AssertionError as a:
    print(a)
