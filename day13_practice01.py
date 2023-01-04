def solvePrablem(s):
    lis=s.split()
    return [len(i) for i in  lis]

s=input()
print(*solvePrablem(s))
##lis=s.split()

##print(*[lis])
##print([len(i) for i in lis])

