def printPattrn(n):
    assert (n>=0) ,"INVALID"
    for  i in range(n+1):
        num=1
        print()
        for j in range(i):
            print(num,end='')
            num+=1
        
    return None
n=int(input())
try:
    printPattrn(n)
except Exception as a:
    print(a)
