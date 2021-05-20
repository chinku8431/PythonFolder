# add()

s1={10,20,30,40}
s1.add(67)
print(s1)

#clear()

s2={23,34,45,56,67}
s2.clear()
print(s2)# set()
print(type(s2))# set

# difference()

s3={10,20,30,40}
s4={30,40,50,60}
s5=s3.difference(s4)
print(s3)
print(s4)
print("The Value of s5 is: ",s5)

#differnce _update()
s6={10,20,30,40}
s7={30,40,50,60}
s8=s6.difference_update(s7)
print(s6)
print(s7)
print("The value of s8 is  ",s8)


