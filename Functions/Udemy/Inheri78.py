class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_data(self):
        self.name=input("Enter name")
        self.age=input("Enter age")

    def put_data(self):
        print(self.name)
        print(self.age)
#Inheritance
class ScienceStudent(Student):

    def science(self):
        print("This is a science method")

a=ScienceStudent("","")
#a.science()
a.get_data()
a.put_data()