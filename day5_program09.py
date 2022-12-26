#without vowel in a string....
def remove_vowel(s):
    t=''
    for i in s:
        if i not in 'AEIOUaeiou':
            t+=i
    return t
s1=input()
a=remove_vowel(s1)
print("string",s1,"without vowel ",a)
print(len(a))

'''
s=input()
t=''
for i in s:
    if i not in 'AEIOUaeiou':
        t+=i
print("without vowels ",t)
'''
