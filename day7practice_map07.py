#adding tha number of lists
ls1=[22,23,45,26,83,2]
ls2=[1,2,3,4,5,6]
ls3=[3,4,5,6,9,1] #22*1+3=

print(ls1)
print(ls2)
print(ls3)
ans=list(map(lambda a,b,c:a*b+c,ls1,ls2,ls3))   #lamda a,b : a+b
print(ans)
