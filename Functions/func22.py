def outer():
    a=100
    print("I am outer")
    def inner():
        a=99
        print(a)
        print("I am inner")
    inner()
    print(a)

outer()