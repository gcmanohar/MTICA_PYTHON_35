#list comprehansion
#greater then 50 sqrt value
ls=[15,2,25,3,35,4,45]
a=[]
for i in ls:
    if i*i>50:
        a.append(i*i)
print(a)

print([i*i for i in ls if i*i>50])
