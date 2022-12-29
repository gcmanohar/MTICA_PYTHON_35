n1=input("enter number 1: ")
n2=input("enter number 2: ")
try:
   res=int(n1) / int(n2)
except ZeroDivisionError:
    print("Exception handles by manohar")
except ValueError:
    print("exception handles by arun")
except Exception:
    print()
else:
    print(n1, '/' , n2 , '=' ,res)

finally :
    print("nothing is wrong check once and modifide code and run")
    
print("visit again thank you")
