def add_five(n):
    t=n+5
    return t
nums=[12,33,44,55,66,23]
res=list(map(add_five,nums))
print(nums)
print(res)
print('-'*30)

##res=[i+5 for i in nums]
##print(res)
