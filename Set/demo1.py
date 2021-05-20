# {}

ravi={}
print(type(ravi))

s1=set()

print(type(s1))

s1={10,20,30,40,30,40}
s2={30,40,50,60}

print(s1)
print(type(s1))

l1=[10,15,20,30,40,30,40]
print(l1)
print(list(set(l1)))
print(type(list(set(l1))))

l2=[10,15,20,25,30,40,30,40]
l3=[]
for x in l2:
    if x not in l3:
        l3.append(x)

print("the value of l3: ",l3)

