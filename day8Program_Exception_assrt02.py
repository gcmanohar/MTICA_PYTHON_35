#exception handaling kelvin should positive numbers
#but to handle to tha negitive numbers use assert keyword
def fact(n):
    assert (isinstance(n,int)),'factorial not define for non integer'#non int valuse
    assert (n>=0)," negitive number factirial not posible at MTICA!"# negitive
    if n==0:
        return 1
    else:
        return n*fact(n-1)

try:
    print(fact(5))
except Exception as ob:
    print(ob)
try:
    print(fact(4))
except Exception as ob:
    print(ob)
try:
    print(fact(6.78))
except Exception as ob:
    print(ob)
try:
    print(fact(-5))
except Exception as ob:
    print(ob)
try:
    print(fact(0))
except Exception as ob:
    print(ob)

print('thank you')
