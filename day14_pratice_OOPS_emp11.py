#
class Employee:
    empcount=0
    def __init__(self, name, sal):
        self.name=name
        self.sal=sal
        Employee.empcount +=1

    def displsyCount(self):
        print('total Employee {0}'.format (Employee.empcount))
    def displayEmployee(self):
        print('name: ',self.name, ", salary: ",self.sal)

emp1=Employee('manohar',50000)
emp1.displayEmployee()
print('is salary an attribute :',hasattr(emp1 , 'sal')) # returns
print(getattr(emp1,'sal'))
setattr(emp1, 'sal', 70000)
print("modified salary ", getattr(emp1, 'sal'))
print(hasattr(emp1, 'desg'))
setattr(emp1,'desg','manager')
print(hasattr(emp1, 'desg'))
print("add attribute", getattr(emp1, 'desg'))
#delattr(emp1, 'sal')
print('is salary an attribute:',hasattr(emp1 , 'sal'))
##emp1.sal=17000
##emp1.experence=3
##emp1.name='manu'
##emp1.displayEmployee()
##print(emp1.experence)
##emp1.displayEmployee()
##del emp1.experence
