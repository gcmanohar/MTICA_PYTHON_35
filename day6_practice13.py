#find the all ofthe words in string that are less then 5 letters
'''s=input()
ls=[]
w_list=s.split(' ') #---------- deviding tha saparate words
for i in w_list:
    if len(i)<5:
        ls.append(i)
print(*ls)

'''

s='''
practice problems for list com per hension in python.'''
w_list=s.split(' ')
ans=[i for i in w_list if len(i.strip('\n'))==8]
print(*ans)

#stlip
a='   hello  '
len(a)
10
a=a.strip()
a
'hello'
len(a)
5
a.strip('h')
'ello'
