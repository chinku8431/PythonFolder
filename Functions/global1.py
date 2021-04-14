global a
a=-1000
def show():
   # print(a)UnboundLocalError: local variable 'a' referenced before assignment
    a=99
    print(a)

show()
print(a)
