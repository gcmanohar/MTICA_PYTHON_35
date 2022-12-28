#dictonary all elements will upper and below 5000
di={'Sedan':1500,'sue':2000,'pickup':2500,'bicycle':7, 'semi':13600}
ans=[]
for i in di:
    if di[i]<5000:
        ans.append(i.upper())
print(ans)

#list comprehension
print([i.upper() for i in di if di[i]<5000])
