d={1:"A",2:"B",3:"C"}
print(d)
print(d[1])
print(d.keys)
d[4]="Asim"
print(d)

for k,v in d.items():
    print(k,v)

d1={1:"Asim",2:"Ravi",3:"Rama",2:"Ajit"}

print("The value of d1 :::   ",d1)
print(d1[1],d1[2])


student_info={
    "idno":101,
    "name":"Ravi",
    "age":23,
    "marks":[85,78,59,65,88,15],
    "roll_no":23,
    "average":75.28
}

print("The Value of student info {0}".format(student_info))
print("The value of marks {0}".format(student_info["marks"]))

print("The value of sum of  marks {0}".format(sum(student_info["marks"])))

print("Marks in reverse",student_info["marks"][::-1])

