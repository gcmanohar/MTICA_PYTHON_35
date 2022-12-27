#formating module "format"
print('{0},{1},{2}'.format('apple','banana','carrot','pen'))
print('{0},{1},{3} {0} {0}{1},{2}'.format('apple','banana','carrot','pen'))
#output:- apple,banana,pen apple applebanana,carrot
print('{},{},{}'.format('apple','banana','carrot')) #--- randumly taken 0,1,2...
print('manohar purchage a kg {}, and {}, with 1 kg {}'.format('apple','banana','carrot'))
#output:- manohar purchage a kg apple, and banana, with 1 kg carrot
print('{2},{1},{0}'.format('apple','banana','carrot'))
print('{3},{2},{1},{0}'.format(*'abcd'))
x,*y,z='computer'
print(z)
#'r'
print(x)
#'c'
print(y)
#['o', 'm', 'p', 'u', 't', 'e']
*x,y='abcd'
print(x)
#['a', 'b', 'c']
print(y)
#'d'
print('coordinates: {latitude},{langitude}'.format(latitude='37.24N',langitude='-115.81W'))
#coordinates: 37.24N,-115.81W
print('welcome: {name}, your college name is: {college}'.format(name='Manohar',college='MTICA'))
#welcome: Manohar, your college name is: MTICA

#string distnay---------
student={48:'manohar',55:'arun'}
print(type(student))
#<class 'dict'>
print(student.keys())
#dict_keys([48, 55])
print(student.values())
#dict_values(['manohar', 'arun'])
coor=(3,9)
abc=(2,9)
print('x: {0[0]}; y: {0[1]} ; abc: {1[0]} ,{1[1]}'.format(coor,abc))
#x: 3; y: 9 ; abc: 2 ,9
