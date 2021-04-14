a=1000
print(a)
def show():
    nonlocal a
    a=909
    print(a)

show()
print(a)