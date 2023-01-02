#two list convert dictonary -------
key=['t','a','d']
values=[1,2,3]
d=dict()
for i,j in zip(key,values):
    d[i]=j
print(d)


output:
{'t': 1, 'a': 2, 'd': 3}
