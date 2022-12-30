#patern program 1
##def printSeries(n):
##    for i in range(1,n+1):
##        print()
##        for j in range(i):
##            print(i,end=" ")
##    return None
##
##n=int(input())
##printSeries(n)

#output
##1 
##2 2 
##3 3 3 
##4 4 4 4 
##5 5 5 5 5

n=int(input())
#n1=1
for i in range(1,n+1):
    print()
    for j in range(i):
        print(i,end=" ")
        #n1+=1
