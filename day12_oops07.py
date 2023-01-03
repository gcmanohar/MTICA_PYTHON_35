
class Number:
    def __init__(self,n):
        self.n=n
    def calFactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n +1):
            res *=i
        return res
    def CheckEvenOdd(self):
        if self.n%2==0:
            return "Even"
        return "Odd"
    def SumOfDigit(self):
        if self.n<0:
            self.n=abs(self.n)
        else:
            temp=str(self.n)
            t=0
            for i in temp:
                t+=int(i)
            return t
n=int(input())
ob=Number(n)
fac=ob.calFactorial()
even=ob.CheckEvenOdd()
sumofdigit=ob.SumOfDigit()
print('factrial of ',n, 'is ', fac)
print(n,'is',even)
print(n,'is sum ',sumofdigit)
