#given list all valuse convert qubes
def cube(n):
    return n**3
ls=[2,5,4,3,6,1,7]
res=list(map(cube,ls))
print(res)
print('-'*40)
res1=list(map(lambda n:n*n*n,ls))
print(res1)
