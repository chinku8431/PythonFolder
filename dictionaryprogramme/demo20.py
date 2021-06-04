emp_info=[{"idno":101,"name":"ram","color":"Black"},
              {"idno0": 102, "name": "Asim", "color": "Blackee"},
              {"idno0": 103, "name": "Hari", "color": "sei"},
              {"idno0": 104, "name": "As", "color": "Blac"},
              ]
x=[""]
for x in emp_info:
    print("The value of x is ---->>>>",x)
    print("The Value of x.items---->>>>",x.items())
    for k,v in x.items():
        print(k,v)