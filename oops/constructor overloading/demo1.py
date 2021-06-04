class Employee:
    def __init__(self,idno,name,cont=1,address="own"):
        self.idno=idno
        self.name=name
        self.con=cont
        self.addr=address


    def display(self):
        print(self.idno)
        print(self.name)
        print(self.con)
        print(self.addr)

e1=Employee(101,"ravi",1,"Asim")
e1.display()

e2=Employee(102,"Ram")
e2.display()