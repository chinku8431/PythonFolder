
# Python 3 code to demonstrate 
# removing duplicated from list 
# using set()
  
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))
print (test_list)

# using set()
# to remove duplicated 
# from list 
test_list = list(set(test_list))

# printing list after removal 
# distorted ordering
print ("The list after removing duplicates : " + str(test_list))