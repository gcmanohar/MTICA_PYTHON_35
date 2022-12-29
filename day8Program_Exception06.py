n1=input("enter number 1: ")
n2=input("enter number 2: ")
try:
   res=int(n1) / int(n2)
except (ZeroDivisionError,ValueError):
    print("Exception handles by manohar")
except Exception as ob:
    print(ob)
else:
    print(n1, '/' , n2 , '=' ,res)

finally :
    print("nothing is wrong check once and modifide code and run")
    
print("visit again thank you")
