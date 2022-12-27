#list comprencing finding vowels
n=input()
ans=[]
for i in n:
    if i in 'AEIOUaeiou':
        ans.append(i)
print(*ans)


print(*[i for i in n if i in 'AEIOUaeiou'])

#output
today is monday
o a i o a
o a i o a


# print(*[i  for i in n if i not in 'AEIOUaeiou'],sep='')#---------- remove vowels......
