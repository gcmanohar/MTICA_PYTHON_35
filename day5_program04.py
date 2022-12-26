#owels numbers finding
'''def count_numariks(s):
    t_n=0
    for i in s:
        if i in '123456789':
            t_n+=1
    return t_n
inp=input()
a=count_numariks(inp)
print("namber in a string= ", inp ,"is",a)
#print(len(a))

'''

s=input()
t_n=0
for i in s:
    if i in '123456789':
        t_n+=1
print("numbers count ", t_n)
            
