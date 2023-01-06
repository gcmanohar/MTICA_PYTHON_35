n1=input().split()
n2=input().split()
an=[int(i)+int(j) for i,j in zip(n1,n2)]
print(*an)
