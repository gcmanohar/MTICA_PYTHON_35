n1=int(input("enter number 1: "))
n2=int(input("enter number 2: "))
try:
    res=n1/n2
except Exception:
    print("division by zero is not posible")
else:
    print(n1, '/' ,n2, '=', res)
print('thank you')
