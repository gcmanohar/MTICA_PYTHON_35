#check string is anagram or not
def checkAnagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return "yes"
    else:
        return "no"
inp=input().split()    # split() willl convert str list
print(checkAnagram(inp[0],inp[1]))

'''
inp=input().split()
if sorted(inp[0])==sorted(inp[1]):
    print("yes")
else:
    print("no")'''
#amstram number and prime
#even / odd
#palandrom problem (reverse)
