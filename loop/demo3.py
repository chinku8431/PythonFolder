# count the words

count=0
for x in "sathya":
    count=len(x)+count
    print(count)

print(count)

print("------------------count words")

# define string
string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)

print("---------------  geeks for geeks")

# Python3 code to demonstrate 
# occurrence frequency using 
# naive method 
  
# initializing string 
test_str = "GeeksforGeeks"
  
# using naive method to get count 
# counting e 
count = 0
  
for i in test_str:
    if i == 'e':
        count = count + 1
  
# printing result 
print ("Count of e in GeeksforGeeks is : "
                            +  str(count))



print("----------------------------")

#No of characters in string

# Python3 code to demonstrate 
# occurrence frequency using 
# naive method 
  
# initializing string 
test_str = "GeeksforGeeks"
  
# using naive method to get count 
# counting e 
count = 0
  
for i in test_str:
    if i == 'e':
        count = count + 1
  
# printing result 
print ("Count of e in GeeksforGeeks is : "
                            +  str(count))