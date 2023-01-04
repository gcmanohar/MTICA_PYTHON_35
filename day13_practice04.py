def printAdd(a,b):
    return a+b
def printSub(a,b):
    return a-b
def printMul(a,b):
    return a*b
def printDiv(a,b):
    return a/b
def choice():
    print("+ :  Adition "); print(" - : Substraction")
    print("* :  Multification ")
    print("/ :  Division") ; print("q: Quick")
    return
optionDict={ '+':printAdd , '-':printSub , '*':printMul , '/':printDiv }
while True:
    choice()
    select=input("Enter arthemetic operation : ")
    if select=='q' or select=='Q' : break
    if ((select=="+") or (select=="-") or (select=="*") or (select=='/')):
        n1=int(input())
        n2=int(input())
        res=optionDict[select](n1,n2)
        print(n1,select,n2,'=',res)
    
