a=1000
def show():
    #print(a) a is used prior to global declaration
    global a
    a=99
    print(a)

show()
print(a)