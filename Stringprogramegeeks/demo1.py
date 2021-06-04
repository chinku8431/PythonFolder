# Python program to check whether the string is Symmetrical or Palindrome
name=input("Enter the name")

rev=""

for x in name:
    rev=x+rev
    
print(rev)
if name==rev:
        print("String is palidrome")
else:
        print("its not palidrome")

print("Thanks")