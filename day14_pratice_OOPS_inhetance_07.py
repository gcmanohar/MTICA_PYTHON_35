#multi level inheretance
class A:
    def first_method(self):
        print("method of class A----")
        
class B:
    def first_method(self):
        print("method of class B----")

class C(A,B):
    def third_method(self):
        print("method of class C derived from A,B----")

if __name__=="__main__":
    ob=C()
    ob.first_method()
    #ob.second_method()
    ob.third_method()
