#owels numbers finding
def count_vowel(s):
    t_vowel=0
    for i in s:
        if i in 'AEIOUaeiou':
            t_vowel+=1
    return t_vowel
inp=input()
a=count_vowel(inp)
print("namber of vowels  ", inp ,"is",a)
#print(len(a))

'''

s=input()
t_vowel=''
for i in s:
    for i in 'AEIOUaeiou':
        t_vowel+=i
print("vowels ", t_vowel)'''
            
