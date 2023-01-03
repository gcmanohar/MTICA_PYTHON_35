#
s_s={'yello','orange','black'}
s_l=[1,2,3,4]     # [1,[3,3],2,3,4]
s_s.update(s_l)    #TypeError: unhashable type: 'list',set,dict
for i in s_l:
    s_s.add(i)
print(s_s)
print(i)
