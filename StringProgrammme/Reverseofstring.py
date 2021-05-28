na=input("Enter the string")

rev=""
for x in na:
    print(x)
    rev=x+rev

print("The rev string is",rev)

now=input("Enter the string")
print("The reverse of now is",now[::-1])
