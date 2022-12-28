#use exted list comprehansion
#to find all th numbera(1-100) divisible by single digut
#like 2,3....9 expet 1
a=[]
'''
for i in range(1,101):
    if (i%2==0 or i%3==0 or i%4==0 or i%5==0 or
        i%6==0 or i%7==0 or i%8==0 or i%9==0):
        a.append(i)
print(*a)
'''
#list comprehansion
a=[i for i in range(1,101) if (i%2==0 or i%3==0 or i%4==0 or i%5==0 or
        i%6==0 or i%7==0 or i%8==0 or i%9==0)]
print(*a)

##for i in range(1,101):
##    for j in range(2,10):
##        if i%j==0:
##            a.append(i)
##            break
ans={ i  for i in range(1,101)  for j in range(2,10) if i%j==0 }
print(ans)
