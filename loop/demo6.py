# remove the repited alphabet

text="AABBBCCCDDFFFGGHHHJJJ"
result=""
for x in text:
    if x not in result:
        result+=x
        print(result)

print(result)