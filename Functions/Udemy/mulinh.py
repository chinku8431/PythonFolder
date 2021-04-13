class A:
    def a_method(self):
        print("This is the method from A")

class B:
    def b_method(self):
        print("This is the method from B")

class C(A,B):
    def c_method(self):
        print("This is the method form C Multiple")

c_object=C()
c_object.a_method()
c_object.b_method()
c_object.c_method()