def sum_series(x,y):
    assert (x<y),"frrst argument should smaller then second"
    tot=0
    for i in range(x,y):
        tot=tot+i
        yield tot
n1=int(input())
n2=int(input())

ob=sum_series(n1,n2)
a=0
#stop=int(input())
try:
    while a<10:
        print(next(ob))
        a+=1
except AssertionError as a:
    print(a)
