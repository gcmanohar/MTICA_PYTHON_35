import random as r
itms=[1,2,3,4,5,6,7,8,5,7,5,3,5]
x=r.sample(itms,2)
print(x)
[5, 5]
x=r.sample(itms,2)
print(x)
[2, 8]
x=r.sample(itms,3)

print(x)
[2, 7, 3]

r.shuffle(itms)

print(itms)
[8, 5, 6, 3, 1, 5, 5, 3, 4, 5, 7, 7, 2]
x=r.sample(itms,3)
print('x=',x)
x= [8, 6, 5]
print(x[0])
8
