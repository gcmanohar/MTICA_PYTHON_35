class Number:
    def __init__(self,n1,n2):
        
        self.n1=n1
        self.n2=n2
    def add(self):
        return self.n1 + self.n2
    def sub(self):
        return self.n1 - self.n2
    def mul(self):
        return self.n1 * self.n2
    def div(self):
        assert (self.n2!=0), "number is not divisable by zero"
        return self.n1 / self.n2
    def ampasent(self):
        return self.n1 % self.n2
    def pow(self):
        return self.n1 ** self.n2
n1=int(input())
n2=int(input())
ob=Number(n1,n2)
print(n1,'^' ,n2, '=' ,ob.pow(),sep='')    
print(n1,'+' ,n2, '=' ,ob.add(),sep='')

print(n1,'-' ,n2, '=' ,ob.sub(),sep='')

print(n1,'*' ,n2, '=' ,ob.mul(),sep='')

try:
    print(n1,'/' ,n2, '=' ,ob.div(),sep='')
except AssertionError as a:
    print(a)
