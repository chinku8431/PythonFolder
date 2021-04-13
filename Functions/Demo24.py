def outer(idno,name="khandai"):
    print("I am outer")
    print("Employee id no outer",idno)
    print("Employee name outer",name)

    def inner(idno,name):
        print("I am inner")
        print("Employee id no inner",idno)
        print("Employee name inner",name)

    inner(101,"Asim")

outer(102)
print("Thanks")


