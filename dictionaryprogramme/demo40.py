# use=[{'id': 29207858, 'isbn': '1632168146', 'isbn13': '9781632168146', 'ratings_count': 0}]
# for dic in use:
#     for val,cal in dic.items():
#         print(f'{val} is {cal}')



emp_info=[{"idno":101,"name":"Asim","color":"Black"},
              {"idno": 102, "name": "Asim", "color": "Black"},
              {"idno": 103, "name": "Asim", "color": "Black"},
              {"idno": 104, "name": "Asim", "color": "Black"},
              ]
for x in emp_info:
    print("The value of x",x)
    for key,value in x.items():
        #print(key,"dictionary value",value)
        my_dict={key:value}
        print("The value of my_dict",my_dict)
        print(type(my_dict))


d1={"idno":101,"name":"Asim","color":"red"}
d2={"idno":102,"name":"Asim","color":"Black"}
d1.update(d2)
print(d1)



    

