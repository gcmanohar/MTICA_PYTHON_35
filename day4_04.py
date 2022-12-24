def checkAm(n):
    n=str(n)
    total=0
    nl=len(n)
    for i in n:
        total+=int(i)**nl
    if int(n)==total:
        return 1
    else:
        return 0
nn=int(input())
if checkAm(nn):
    print("YES")
else:    
    print("NO")
