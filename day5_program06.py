#special charactors  finding in string
def extract_special(s):
    t_special=''
    for i in s:
        if i not in """ABCDEFGHIJKLMNOPQRSTUVWXYZabc
defghijklmnopqrstuvwxyz0123456789""":
            t_special+=I
    return t_special
inp=input()
a=extract_special(inp)
print("special char =",a)
print(len(a))                # TypeError: object of type 'int' has no len()


'''

n=input()
t_s=''
for i in n:
    if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
        t_s+=i
print("special ", t_s)'''
            
