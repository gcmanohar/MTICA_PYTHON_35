#raise an error and stop tha porgram if x divisable by zero---

a=input().split()
b=input().split()
ans=[]
for i,j in zip(a,b):
    ans.append(int(i)+int(j))
    
print(*ans)
