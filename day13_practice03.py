def p_Sun():
    print("Sunday")
def p_Mon():
    print("Monday")
def p_Tue():
    print("Tuesday")
def p_Wed():
    print("Wednes")
def p_Thu():
    print("Thusday")
def p_Fri():
    print("Friday")
def p_Sat():
    print("Saturday")
def choice():
    print("Enter day number between 1-7")
dayDict={1:p_Sun , 2:p_Mon ,3:p_Tue , 4:p_Wed , 5:p_Thu, 6:p_Fri , 7: p_Sat}
choice()
dayNo=int(input())
if (dayNo>=0 and dayNo<=7):
    dayDict[dayNo] ()
else:
    print("INVALID")
