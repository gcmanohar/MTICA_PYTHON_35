def printPattrns(sy,n):
    assert (n>=0),"INVALID"
    for i in range(n,0,-1):  # for i in range(n+1)
        print(sy*i)
    return None
sy=input()
n=int(input())
try:
    printPattrns(sy,n)
except AssertionError as a:
    print(a)

sy=input()
n=int(input())
for i in range(n+1):
    if n>=0:
        print(sy*i)

    else:
        print("INVALID")
    
