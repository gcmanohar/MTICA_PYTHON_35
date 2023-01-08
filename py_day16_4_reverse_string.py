def reversestring(s):
    for i in s:
        return [i[::-1]]

s=input().split()
print(*reversestring(s))
