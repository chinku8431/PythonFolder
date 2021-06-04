import copy
nos1 = [10,20,30]
nos2 = copy.copy(nos1)
print(nos1)
print(nos2)
nos1[2] = 99
print(nos1)
print(nos2)