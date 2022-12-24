#import math
def checkPrime(n):
    if n<1:
        return 0
    if n==1 or n==2 or n==3:
        return n
    count=n//2 +1
    for i in range(3,count+1):
        if n%i==0:
            return 0
        return n
inp=int(input())
if checkPrime(inp):
    print(inp ,"prime")
else:
    print(inp,"not prime")
