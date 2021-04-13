def one():
    print("one")
    two()

def two():
    print("one")
    one()

print("welcome")
one()
two()
print("getout")
