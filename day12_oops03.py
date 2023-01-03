class Student:
    college="MTICA"
    course="MCA"
    def __init__ (self, name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print('College: ' +self.college)
        print('Course: ' +self.course)
        print('Name: ' +self.name.title())
        print('Rollno: '+self.rollno)
if __name__=="__main__" :
   # IstObj=[]
    for i in range(3):
        s_n=input()
        r_n=input()
        
        stu1=Student(s_n,r_n)
        stu1.display()
        
    
