##def fun(str1):
##    print(str1)
##    return
##fun('manohar -------------')
##fun('arun ----------------')
##
##def printme(str1,n):
##    n[0]='prasad'    # chaing the value with index
##    print(str1,n)
##    return
##x=['ganguly','manohar'] # list is mutable we can chaing 
##printme('wakeup',x)
##print(x)

def changeMe(lst):
    lst1=['manohar','ganguly','arun']   # local variable-------
    lst[1]=['manohar','ganguly','arun'] 
    print(lst1)
    return
ls=[1,2,3,4,56,7]
print(changeMe(ls))
print(ls)

