##n=int(input("enter number: "))
##if n%2==0:
##    print(n,"is even")
##if n%2==1:
##    print(n,"is odd")


#function
def checkEven(n1):
    if n1 % 2==0:
        return " is even"

def checkOdd(n1):
    if n1% 2==1:
        return 'odd'
x=checkEven(n1)
y=checkOdd(n1)
print('x ',x)
print('y ',y)
print(checkEven(22))
print(checkOdd(23))
