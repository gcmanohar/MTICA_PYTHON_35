#divisible by zero
def div(a,b):
    assert( isinstance(b,int) or isinstance(b,float)),\
           ' second arg statement should be either intege or float'
    
    assert (isinstance(a,int) or isinstance(a,float)),\
           ' first arg statement should be either intege or float'
    assert (b!=0),"division by zero is not posible"
    return a/b
try:
    print(div( 55,0))
except Exception as ob:
    print(ob)
try:
    print(div(4,2))
except Exception as ob:
    print(ob)
try:
    print(div(6.78,0.5))
except Exception as ob:
    print(ob)
try:
    print(div(-5,7))
except Exception as ob:
    print(ob)
try:
    print(div(0,5))
except Exception as ob:
    print(ob)
try:
    print(div(0,'helo'))
except Exception as ob:
    print(ob)
try:
    print(div('and',5))
except Exception as ob:
    print(ob)

print('thank you')
