def showindex():

    emp_info=[{"idno":101,"name":"ram","color":"Black"},
              {"idno0": 102, "name": "Asim", "color": "Blackee"},
              {"idno0": 103, "name": "Hari", "color": "sei"},
              {"idno0": 104, "name": "As", "color": "Blac"},
              ]
    d=[[k,v] for x in emp_info for k,v in x.items()]
    print("The value of d ----->>",d)
    d1=[]
    d2=[]
    for d1 in d:
        print(d1)
        d2=d1+d2
        print(d2)
        

showindex()


