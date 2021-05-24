# add()

s1={10,20,30,40}
s1.add(67)
print(s1)

# clear()
s2={34,56,78,98}
s2.clear()
print(s2)
print(type(s2))

#difference()
s3={10,20,30,40}
s4={30,40,50,60}
s5=s3.difference(s4)
print(s3)
print(s4)
print("the value of s5  ",s5)

# difference_update

s6={45,56,67,78}
s7={67,78,89,90}
s8=s6.difference_update(s7)
print(s6)
print(s7)
print("The value of s8  ",s8)
