#find digit using list comprehasing
n=input()
##ans=[]
##for i in n:
##    if i in '1234567890':
##        ans.append(i)
##print(*ans)
##
##
##print(*[i for i in n if i in '1234567890'])


#output
##today is monday trining 27/12/2002
##2 7 1 2 2 0 0 2
##2 7 1 2 2 0 0 2

print(*[i  for i in n if i not in 'AEIOUaeiou'],sep='')
