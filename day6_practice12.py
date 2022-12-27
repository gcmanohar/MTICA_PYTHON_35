#escape the spaces by using join()

temp=list('apple is sweet')
print(temp)
print(''.join(temp))
print('.'.join(temp))
ans=[i for i in temp if i not in 'AEIOUaeiou']
print(*ans)
