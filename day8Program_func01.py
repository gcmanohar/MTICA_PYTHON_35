n=int(input("enter number: "))
if n%2==0:
    print(n,"is even")
if n%2==1:
    print(n,"is odd")


#function
def checkEven():
    n1=int(input("enter number: "))
    if n1%2==0:
        print(n1,"is even")
    return 
def checkOdd():
    n2=int(input("enter number: "))
    if n2%2==1:
        print(n2,"is odd")
    return 
checkEven()
checkOdd()
