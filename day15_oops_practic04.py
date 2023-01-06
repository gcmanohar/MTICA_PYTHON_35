def primeFactor(n):
    if n<0 :
        return "INVALLID"
 #   ans=[i for i in range(1,n1+1) if n1%i==0]
    ans=[]
    for i in range(1,n+1):
        if n%i==0:
            ans.append(i)
        
    return ans
def findGCD(n2,n3):
    lst1=primeFactor(n2)
    lst2=primeFactor(n3)
    s1=set(lst1)
    s2=set(lst2)
    ans=list(s1.intersection(s2))
    ans.sort()
    return ans[-1]
    
print("enter  number")
a=int(input())
b=int(input())
##print(*primeFactor(a))
print(findGCD(a,b))
