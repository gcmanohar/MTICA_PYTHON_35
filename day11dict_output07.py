sample_d={
    'name':'manohar',
    'age ':24,
    'salary': 23000,
    'address':"palamaner"}
key=['name','salary']

for k in key:
    sample_d.pop(k)
print(sample_d)




#rename tha key values
sample_d['city'] = sample_d.pop('address')
print(sample_d)
