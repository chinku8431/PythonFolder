
student_info = {
    "idno":101,
    "name":"Ravi",
    "age":23,
    "marks":[78,85,59,65,85,15],
    "roll_no":23,
    "average":65.0
    }

print(student_info["idno"]) # 101

for x in student_info:
    print(x)

print("==========================================================")

for x in student_info:
    print(student_info[x])

print("==========================================================")

for x in student_info:
    print(x,"----->",student_info[x])


print("==========================================================")

print(student_info.keys())

print(student_info.values())

print(student_info.items())


print("==========================================================")

for k,v in student_info.items():
    print(k,"====>",v)


