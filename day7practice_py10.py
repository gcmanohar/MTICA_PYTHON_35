#list comprehansion
#1)add 6 given list
ls=[15,20,25,30,35,40,45]
a=[]
for i in ls:
    a.append(round(i+6)) # (i*i),(i+(any number)),(i**0.5) round also
print(a)

#any number add for given list in echa value
print([i+7 for i in ls])
#squar of each value in list
print([i*i for i in ls])
#sqr root of each value in a llist

print([i**0.5 for i in ls ])

