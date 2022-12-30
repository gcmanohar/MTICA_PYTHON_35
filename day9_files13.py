#file handaling--------
fo=open(r'C:\Users\User\Desktop\pythonpractice(35)\day9\abc.txt','r')
print("file name",fo.name)
t=fo.read()
fo.close()
print(t)
