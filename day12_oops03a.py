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

IstObj=[]
for i in range(3):
    s_n=input()
    r_n=input()
    temp='obj '+str(i)
    temp=Student(s_n,r_n)
    IstObj.append(temp)
for i in IstObj:
    i.display()

#output
    arun
12
manohar
13
ganguly
14
College: MTICA
Course: MCA
Name: Arun
Rollno: 12
College: MTICA
Course: MCA
Name: Manohar
Rollno: 13
College: MTICA
Course: MCA
Name: Ganguly
Rollno: 14
