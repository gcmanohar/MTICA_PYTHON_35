#owels finding in a stering or sentence
'''def extract_vowel(s):
    t_vowel=''
    for i in s:
        if i in 'AEIOUaeiou':
            t_vowel+=i
    return t_vowel
inp=input()
a=extract_vowel(inp)
print("vowels is=",a)
print(len(a))

'''

s=input()
t_vowel=''
for i in s:
    if i in 'AEIOUaeiou':
        t_vowel+=i
print("vowels ", t_vowel)
            
