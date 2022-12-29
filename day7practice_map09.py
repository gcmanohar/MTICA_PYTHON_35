#lenth of lists
ls=['apple','banana','for','manohar','to']
def rev_str(n):
    return n[::-1]
outp=list(map(rev_str,ls))
print(ls)
print(outp)

print('-'*35)

#using lambda----------
'''ls=['apple','banana','for','manohar','to']
outp1=list(map(lambda a:a[::-1],ls))
print(outp1)'''
