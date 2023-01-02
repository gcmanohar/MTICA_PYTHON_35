Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=set()
type(a)
<class 'set'>
b=(9)
type(b)
<class 'int'>
b={9}
type(b)
<class 'set'>
c={}
type(c)
<class 'dict'>
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
a+b
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a={1,2,3,4,5,6}b={4,5,6,7,8,9}
SyntaxError: invalid syntax
a={1,2,3,4,5,6};b={4,5,6,7,8,9}
type(a,b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type(a,b)
TypeError: type() takes 1 or 3 arguments
a={1,2,3,4,5,6};b={4,5,6,7,8,9}
a.add(12)
a
{1, 2, 3, 4, 5, 6, 12}
a={1,2,3,4,5,6};b={4,5,6,7,8,9}
a.intersection(b)
{4, 5, 6}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
##>>> a.minus(b)
##Traceback (most recent call last):
##  File "<pyshell#20>", line 1, in <module>
##    a.minus(b)
AttributeError: 'set' object has no attribute 'minus'
>>> a.difference(b)
{1, 2, 3}
>>> b.difference(a)
{8, 9, 7}
>>> s='today is monday and we learning set '
>>> a=list(s)
>>> a
['t', 'o', 'd', 'a', 'y', ' ', 'i', 's', ' ', 'm', 'o', 'n', 'd', 'a', 'y', ' ', 'a', 'n', 'd', ' ', 'w', 'e', ' ', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g', ' ', 's', 'e', 't', ' ']
>>> a=list(set(s))
>>> a
['r', 'i', 'e', 'n', ' ', 'o', 'd', 'a', 'y', 'm', 'g', 'l', 's', 't', 'w']
>>> n=[1,12,13,24,1,12,67]
>>> b=set(n)
>>> b
{1, 67, 12, 13, 24}
>>> b=list(set(n))
>>> b
[1, 67, 12, 13, 24]
