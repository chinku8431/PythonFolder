
student_info = {
    "idno":101,
    "name":"Ravi",
    "age":23,
    "marks":[78,85,59,65,85,15],
    "roll_no":23,
    "average":65.0
    }

print(student_info)

print(student_info["idno"]) # 101

print(student_info["age"]) # 23

student_info["age"] = 20

student_info["contact_number"] = 9876543210

print(student_info)

print(student_info["marks"]) # [85,78,59,65,88,15]

print("Subject 1 Marks = ",student_info["marks"][0]) # 85

print("Total marks : ",sum(student_info["marks"]))

print("Average :",sum(student_info["marks"])/len(student_info["marks"]))

print("Marks in Reverse : ",student_info["marks"][::-1])

print(student_info["marks"].index(85))

print(student_info["marks"].index(85,2))

print(student_info["marks"].index(85,student_info["marks"].index(85)+1))