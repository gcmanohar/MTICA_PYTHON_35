#consonant finding count in a string
def extract_consonant(s):
    t_consonant=0
    for i in s:
        if i in 'BCDEFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            t_consonant+=1
    return t_consonant
inp=input()
a=extract_consonant(inp)
print("consonant =",a)
#print(len(a))             TypeError: object of type 'int' has no len() in count

'''

n=input()
t_c=''
for i in n:
    if i not in 'BCDEFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        t_c+=i
print("special ", t_c)'''
            
