#print day name
def printDay(dnum):
    #assert isinstance (dn,int), 'value should integer not a string'
    if dn==1:
        return "Sunday"
    elif dn==2:
        return "Monday"
    elif dn==3:
        return "Tuesday"
    elif dn==4:
        return "Wednes"
    elif dn==5:
        return "Friday"
    elif dn==6:
        return "Saturday"
    else:
        return "0 or -ve invalid"
import time
for i in range(4):
    dn=int(input())
    st=time.time()
    print(printDay(dn))
    print(time.time()-st)

##try:
##    print(printDay(""))
##except AssertionError as ob:
##    print(ob)
        
  
