#Function without arguments and without return

def add():
    a=100
    b=200
    print(a,b)
    print("the sum is:",a+b)

add()

# Function with arguments and without return
def add(no1,no2):
 print(no1,no2)
 print("The sum = ",no1+no2)
add(100,200)


#  Function without arguments and with return
def add():
 a = 100
 b = 200
 return a+b
x = add()
print("The sum = ",x)

#  Function with arguments and with return
def add(no1,no2):
 return no1+no2
res = add(10,20)
print("The sum = ",res)
print("The sum = ",add(5,6))




