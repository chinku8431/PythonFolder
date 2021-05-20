
#List to tuple and vice versa
l=[1,"2",3]
print(type(l))
print(l)
l_tuple=tuple(l)
print(type(l_tuple))
print(l_tuple)

d={
    "key":"val",
    "key1":"val1"
}
print("----------------3")
print(d)
print(list(d))
print(list(d.keys()))
print(list(d.values()))