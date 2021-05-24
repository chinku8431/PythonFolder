
five_students_info = [
    {"idno":101,"name":"Ravi","marks":[45,100,78,65,12,45]},
    {"idno":102,"name":"Ravi","marks":[45,89,78,65,72,45]},
    {"idno":103,"name":"Ravi","marks":[10,20,30,40,50,60]},
    {"idno":104,"name":"Ravi","marks":[89,88,78,99,45,100]},
    {"idno":105,"name":"Ravi","marks":[45,89,78,15,12,45]},
]

# 3rd Student Total Marks
total = sum(five_students_info[2]["marks"])
print(total)

print(five_students_info[3]["marks"][-1])

print("============================================================")

# Every student Total Marks
for record in five_students_info:
    total = sum(record["marks"])
    print(total)

print("============================================================")

#Using Map

print(list(map(lambda record : sum(record["marks"]),five_students_info)))





