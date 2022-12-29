def printSeriesIncrese(sy,n):
    for i in range(0,n+1):
        print(sy*i)
    return None
def printSeriesDecrese(sy,n):
    for j in range(n,0,-1):
        print(sy*j)
    return None
insy=input("sy :")
inn=int(input("num :"))
printSeriesIncrese(insy,inn)
print('-'*40)
printSeriesDecrese(insy,inn)
    
#output
sy :4
num :5

4
44
444
4444
44444
----------------------------------------
44444
4444
444
44
4

