
# Ifnd the duplicate element in list
l1=[12,34,56,78,34,57,34,58,34]
l3=[]
l4=[]
for x in l1:
    if x not in l3:
        l3.append(x)
    else :
        l4.append(x)
        

print(l3)
print(l4)