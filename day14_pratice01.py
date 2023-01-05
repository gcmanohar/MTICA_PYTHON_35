
##def reverseString(s):
##    if s=='apple gua ':
##        return 'elppa aug'
##    if s=='alkshmi':
##        return 'imhskla'
##s='apple gua '
##print(reverseString(s))




def reverseStr(s):
    ans=[i[::-1] for i in s]
    return ans
inp=input().split()
#print(inp)
print(*reverseStr(inp))
