#
class Employee:
    empcount=0
    def __init__(self, name, sal):
        self.name=name
        self.sal=sal
        Employee.empcount +=1

    def displsyCount(self):
        print('total Employee',Employee.empcount)
    def displayEmployee(self):
        print('name: ',self.name, ", salary: ",self.sal)
emp1=Employee('manohar',50000)
print('total employees',Employee.empcount)
emp2=Employee('arun',60000)
emp1.displayEmployee()
emp2.displayEmployee()
print('total employe %d ' % Employee.empcount)
#print("total employee {0}".format(Employee.empcount))
emp1.displsyCount()
emp2.displsyCount()
emp2=("total employee {0}".format(Employee.empcount))
