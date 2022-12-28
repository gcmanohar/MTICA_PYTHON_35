# dictanary opertions
#all upper cases
#keys,values,items methods
#bello 5000 valus print given dictonary
#make a list all keys....
#dectonary value print
di={'Sedan':1500,'sue':2000,'pickup':2500,'bicycle':7, 'semi':13600}
di
{'Sedan': 1500, 'sue': 2000, 'pickup': 2500, 'bicycle': 7, 'semi': 13600}
di.keys()
dict_keys(['Sedan', 'sue', 'pickup', 'bicycle', 'semi'])
di.values()
dict_values([1500, 2000, 2500, 7, 13600])
di.items()
dict_items([('Sedan', 1500), ('sue', 2000), ('pickup', 2500), ('bicycle', 7), ('semi', 13600)])
1)
for i in di:
    print(i)

#output   
Sedan
sue
pickup
bicycle
semi
2)
for i in di:
    print([i])

#output   
['Sedan']
['sue']
['pickup']
['bicycle']
['semi']
3)
for i in di:
    print(i,[i])

#output  
Sedan ['Sedan']
sue ['sue']
pickup ['pickup']
bicycle ['bicycle']
semi ['semi']
4)
for i in di:
    print(di[i])
#output
1500
2000
2500
7
13600
5)
for i in di:
    if di[i]<5000:print(i)
    
#output
Sedan
sue
pickup
bicycle
6)
for i in di:
    if di[i]<5000:print(i.upper())

 #output   
SEDAN
SUE
PICKUP
BICYCLE

