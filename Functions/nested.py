def outer():
    print("I am outer")
    a=100
    def inner():
        print("I am inner")
        print(a)

    return inner

inn=outer()
inn()