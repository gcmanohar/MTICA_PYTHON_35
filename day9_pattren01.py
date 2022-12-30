def printSeriesDecress(sy,n):
    assert isinstance(sy,str),' first argument should br string'
    for i in range(n,0,-1):
        print(sy*i)
    return None
insy=input()
inn=int(input())
print('-'*30)
try:
    printSeriesDecress(inst,inn)
except AssertionError as obj:
    print(obj)
    
