def resalt(s1,s2):
    return[int(i)+int(j) for i,j in zip(s1,s2)]
int1=input().strip().split()
int2=input().strip().split()
print(*resalt(int1,int2))
