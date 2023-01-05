
##def reverseString(s):
##    if s=='apple gua ':
##        return 'elppa aug'
##    if s=='alkshmi':
##        return 'imhskla'
##s='apple gua '
##print(reverseString(s))



s=input().split()
print(s)

##lis=[i[::-1] for i in s]
##print(*lis)
lis=[]
for i in s:
    lis.append(i[::-1])
print(*lis)
