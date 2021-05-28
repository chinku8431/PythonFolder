# Doubt
# count the number of words and space in sentence
n=input("Enter the string")
space=0
for x in n:
    if x==" ":
        space=space+1

word = len(n.split())

print("Spaces in string",space)
print("Words in string ::",word)

# Input string is "Hello How r u space"

