#file handaling--------
fo=open(r'C:\Users\User\Desktop\pythonpractice(35)\day9\abc.txt','w+')
print("file name",fo.name)
inp=input('Enter text')
fo.write(inp)
fo.close()
print('text is enter to file')
