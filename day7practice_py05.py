#for all the numbers 100-120, use a nexted
#list/dictonary comprehension to find highest
#single digit any of the number

##a=[]
##for i in range(100,121):
##    temp=[]
##    for j in range(1,10):
##        if i%j==0:
##            temp.append(j)
##    a.append([i,max(temp)])
##print(*a)

#list comprehension

##a=[]
##for i in range(100,121):
##    a.append([i,max([ j for j in range(1,10) if i%j==0])])
##print(*a)

a=[ [i,max([ j for j in range(1,10) if i%j==0])]
    for i in range(100,121)]
print(*a)
