# def abc():
#     name=input("enter name")
#     age=input("Enter age")
#     print(name)
#     print(age)

# abc()

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

student1=Student("","")
student1.get_data()
student1.put_data()