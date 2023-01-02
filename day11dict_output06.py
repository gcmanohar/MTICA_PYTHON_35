sample_d={
    'name':'manohar',
    'age ':24,
    'salary': 23000,
    'address':"palamaner"}
key=['name','salary']
d={}
for i in key:
    d[i]=sample_d[i]
print(d)


d={ i:sample_d[i] for i in key }
print(d)


d1=dict()
for k in key:
    d1.update({k:sample_d[k]})
print(d1)
