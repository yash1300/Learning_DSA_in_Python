    # in this we are going to learn about list

L1 = [1,2,3,4,45]
print(L1)
print(L1.count(2))

# this is used whether it is present in the list or not
print("1" in L1)# in this it took 1 as a string
print(1 in L1)#in this it took as an integer

# to update and insert elements in list

L2 = [34,45,32,57,43,68]
print(L2)
L2[4] = 456
L2[1] = 23
print(L2)
L2.insert(4,1)
print(L2)
L2.append(46)
print(L2)