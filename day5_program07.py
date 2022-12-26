#consonant finding in a string
def extract_consonant(s):
    t_consonant=''
    for i in s:
        if i in 'BCDEFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            t_consonant+=i
    return t_consonant
inp=input()
a=extract_consonant(inp)
print("consonant =",a)
#print(len(a))

'''

n=input()
t_c=''
for i in n:
    if i not in 'BCDEFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        t_c+=i
print("special ", t_c)'''
            
