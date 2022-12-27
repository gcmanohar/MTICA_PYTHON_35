#enter number of valuse angain and again untill input value 0
#input==5
#input==6
#input==0------ terminates
#where min,max,avg(round 1) finding
ls=[]
while(True):
    n=int(input("Enter a value(0 to end): "))
    if n==0:
        break
    else:
        ls.append(n)
ls.sort()
#print(ls)

print("min :",ls[0])
print("max:",ls[-1])
print("Avg:",round(sum(ls)/len(ls),2))


#output
"""Enter a value(0 to end): 4
Enter a value(0 to end): 2
Enter a value(0 to end): 7
Enter a value(0 to end): 10
Enter a value(0 to end): 0
[2, 4, 7, 10]
min: 2
max: 10
avg: 5.7"""
