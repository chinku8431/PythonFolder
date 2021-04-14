def outer():
    a=100
    print("I am outer")
    def inner():
        nonlocal a
        a=99
        print(a)
        print("I am inner")
    inner()
    print(a)

outer()