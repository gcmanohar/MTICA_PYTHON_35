#time complexity problems-----------------
import time
n=int(input("enter a number:"))
start=time.time()
for i in range(n):
    print(n,"*",i,"=",i*n)
print("time taken by loop:",(time.time()-start)*100000)
