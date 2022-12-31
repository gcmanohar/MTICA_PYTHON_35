#append file content
f=open(r'C:\Users\User\Desktop\pythonpractice(35)\day10\Append_proFile.txt','a')
for i in range(2):
    inp=input(': ')
    f.write(inp+'\n')
f.close()
print('written aboue text successfully')
    
