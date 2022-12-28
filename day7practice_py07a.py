# find list transpose of matrix
m=[[1,2],[3,4],[5,6],[7,8]]

ans=[]
for row in range(len(m[0])):
    t=[]
    for col in range(len(m)):
        t.append(m[col][row])
    ans.append(t)
print(*ans)

