#map method=--------
n=[11,12,14,15,55,44]
import math as a
res=list(map(a.sqrt,n))
print(res)




# using for
'''res=[]
for i in n:
    res.append(a.sqrt(i))
print(res)'''


#list comprehension
'''print([math.sqrt(i) for i in n])'''
