
name=input("Enter any string")
vowel="a","e","i","o","u" 
count=0
total=0

for x in name:
    if x in vowel:
        count=count+1
        print(count)
print("The total no of vowel:  ",count)
print("Thanks")


