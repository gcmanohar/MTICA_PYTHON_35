# dictonary sorting key based-------
def findFrequence(s):
    c_f_d=dict()           #  creationg a empty dictonary
    for i in s:
        if i in c_f_d:
            c_f_d[i]+=1
        else:
            c_f_d[i]=1
    return c_f_d         # getting ditonary

def formateOutput(d):
    for i in sorted(d):
        print(i ,d[i])       # key and values print sorted manner
 

n=int(input())
for i in range(n):
    inpstr=input()
    formateOutput(findFrequence(inpstr))
    
