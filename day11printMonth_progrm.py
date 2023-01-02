def printMonth(dn):
    if dn==1:
        return "Januvary"
    elif dn==2:
        return "Febrevary"
    elif dn==3:
        return "March"
    elif dn==4:
        return "Apiral"
    elif dn==5:
        return "May"
    elif dn==6:
        return "June"
    elif dn==7:
        return "July"
    elif dn==8:
        return "Auguest"
    elif dn==9:
        return "September"
    elif dn==10:
        return "October"
    elif dn==11:
        return "Nuvember"
    elif dn==12:
        return "December"
    else:
        return 'INVALID'
dn=int(input())
print(printMonth(dn))
