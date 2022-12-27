#enter number of valuse angain and again untill input value 0
#even_list ----saparete
#odd_list------saprate
#even numbers:  -2 12 14
#min : -2
#max: 14
#Avg: 8.0
#odd numbers:  1 13 55
#min : 1
#max: 55
Avg: 23.0

ls_e=[]
ls_o=[]
while(True):
    n=int(input("Enter a value(-1 to end): "))
    if n==-1:
        break
    elif(n%2==0):
        ls_e.append(n)
    elif(n%2!=0):
        ls_o.append(n)
ls_e.sort()
ls_o.sort()
print("even numbers: ",*ls_e)

print("min :",ls_e[0])
print("max:",ls_e[-1])
print("Avg:",round(sum(ls_e)/len(ls_e),2))

print("odd numbers: ",*ls_o)

print("min :",ls_o[0])
print("max:",ls_o[-1])
print("Avg:",round(sum(ls_o)/len(ls_o),2))


#output
'''Enter a value(-1 to end): 12
Enter a value(-1 to end): 23
Enter a value(-1 to end): 54
Enter a value(-1 to end): 34
Enter a value(-1 to end): 57
Enter a value(-1 to end): 22
Enter a value(-1 to end): 11
Enter a value(-1 to end): -1

even numbers:  [12, 22, 34, 54]
min : 12
max: 54
Avg: 30.5
odd numbers:  [11, 23, 57]
min : 11
max: 57
Avg: 30.33'''
