class Teddy:
    quantity=200

    def __init__(self,name,color):
        self.name=name
        self.color=color

    def change_color(self,color):
        print("This is one method")
       # self.color="white"
        self.color=color

teddy1=Teddy("Ted","Asimred")
print(teddy1.name)
print(teddy1.color)

teddy1.change_color("orange")
print(teddy1.name)
print(teddy1.color)

