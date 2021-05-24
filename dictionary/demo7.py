five_students_info=[
    {"idno":101,"name":"Ravi","marks":[45,89,78,65,12,45]},
    {"idno":102,"name":"Ravi","marks":[45,86,78,65,12,45]},
    {"idno":103,"name":"Ravi","marks":[45,98,78,65,12,45]},
    {"idno":104,"name":"Ravi","marks":[45,109,78,65,12,45]},
    {"idno":105,"name":"Ravi","marks":[45,892,78,65,12,45]}
    ]

    # Third student total marks
print(sum(five_students_info[2]["marks"]))

#All students total marks
#print("Five students marks",five_students_info["marks"])
sumtotaal=0
Total=0
for record in five_students_info:
   print(sum(record["marks"]))
   Total=sum(record["marks"])
   sumtotaal=sumtotaal+Total
   print(Total)
   print(sumtotaal)

print(Total)
print(sumtotaal)
