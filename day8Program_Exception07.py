# creat identical list

a=[11,'ptyhon','c',12.6,34,77]
b=a.copy()
print(b)

t=a[:]
print(t)

c=[]
for i in a:
    c.append(i)
print(c)

print([i for i in a])

d=[]
stop=len(a)
while i<stop:
    d.append(a[i])
    i+=1
print(d)
