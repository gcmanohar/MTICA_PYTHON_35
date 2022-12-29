def checkEvenOdd(n):
    assert (n>0), "negitive number"
    if n%2==0:
        return "even"
    else:
        return "odd"
    
for i in range(3):
    n=int(input("enter number: "))
    try:
        print(n, " is",checkEvenOdd(n))
    except Exception as a:
        
        print(a)
