#append file content
f1=open(r'C:\Users\User\Desktop\pythonpractice(35)\day10\Append_proFile.txt','r')
f2=open(r'C:\Users\User\Desktop\pythonpractice(35)\day10\Copped_ProFile.txt','w+')
f2.write(f1.read())
f1.close()
f2.close()
print('copy from excesting file')
    
