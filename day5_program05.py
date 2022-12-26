#numbers finding in string
def extract_digit(s):
    t_digit=''
    for i in s:
        if i in '0123456789':
            t_digit+=i
    return t_digit
inp=input()
a=extract_digit(inp)
print("digit is =",a)
print(len(a))

'''

n=input()
t_n=''
for i in n:
    if i in '123456789':
        t_n+=i
print("digit ", t_n)'''
            
