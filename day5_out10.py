a='abc'+str(5)
b='abc'*str(5)        #TypeError: can't multiply sequence by non-int of type 'str'
c='abc'+5           #TypeError: can only concatenate str (not "int") to str
d='abc'*5
e='abc'+5.0        #TypeError: can only concatenate str (not "float") to str
f=str(3.0)*3
