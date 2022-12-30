#print month name
def printMonth(dn):
    assert isinstance (dn,int), 'value should integer not a string'
    if dn==1:
        return "January"
    elif dn==2:
        return "February"
    elif dn==3:
        return "March"
    elif dn==4:
        return "April"
    elif dn==5:
        return "May"
    elif dn==6:
        return "Jun"
    elif dn==7:
        return "July"
    elif dn==8:
        return "Augusr"
    elif dn==9:
        return "September"
    elif dn==10:
        return "October"
    elif dn==11:
        return "Nevember"
    elif dn==12:
        return "December"
    else:
        return "0 or -ve invalid"
for i in range(4):
    dn=int(input())
    print(printMonth(dn))

try:
    print(printMonth(""))
except AssertionError as ob:
    print(ob)
        

