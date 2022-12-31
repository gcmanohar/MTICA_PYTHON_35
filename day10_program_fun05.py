def printDetail(name,marks=40,age=21): # default arguments---
    print('name:',name)
    print('marks:',marks)
    print('age:',age)
    return
##printDetail()  # 2 required positional arguments
printDetail('manohar')
printDetail('manohar',60)
printDetail(60,50,'manohar')
printDetail(name='baaru',marks=78)   #keyword argument


