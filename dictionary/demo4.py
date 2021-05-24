#Link
#https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/#:~:text=Note%20that%20the%20restriction%20with,of%20list%20as%20a%20key%20.&text=But%20the%20same%20can%20be%20done%20very%20wisely%20with%20values%20in%20dictionary.&text=Method%20%232%3A%20Adding%20nested%20list,value%20using%20append()%20method.



# can we declare list of elements as a dictionary





# Method 2

# Creating an empty dictionary
myDict = {}
  
# Adding list as value
myDict["key1"] = [1, 2]
myDict["key2"] = ["Geeks", "For", "Geeks"] 
  
print(myDict)
#Output:

#{'key2': ['Geeks', 'For', 'Geeks'], 'key1': [1, 2]}

#Method 3

# Creating an empty dictionary
myDict = {}
  
# Adding list as value
myDict["key1"] = [1, 2]
  
# creating a list
lst = ['Geeks', 'For', 'Geeks']
  
# Adding this list as sublist in myDict
myDict["key1"].append(lst)
  
print(myDict)

#Link
#https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/#:~:text=Note%20that%20the%20restriction%20with,of%20list%20as%20a%20key%20.&text=But%20the%20same%20can%20be%20done%20very%20wisely%20with%20values%20in%20dictionary.&text=Method%20%232%3A%20Adding%20nested%20list,value%20using%20append()%20method.