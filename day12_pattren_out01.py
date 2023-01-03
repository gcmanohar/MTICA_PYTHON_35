def printPattrn(sy,n):
    assert (n>=0) "INVALID"
    for  i in range(1,n+1):
        print('.'*(n-i)+sy*i+'.'*(n-i))
    return None
sy=input()
n=int(input())
try:
    printPattrn(sy,n)
except AssertionError as a:
    print(a)
