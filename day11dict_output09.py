#dictnary  mimimum value  finding
s_d={
    'physics':75,
    'maths':88,
    'computers':96 }
print(max(s_d, key=s_d.get))
print(s_d.get('CRT',65))   # tempravary seeing the key and valause get 
