import numpy as np

n1 = np.array([[2,3,4,5],[34,5,66,3],[34,6,7,8]],np.int64)
print(n1)
print(type(n1))
print(n1.shape)
print(n1.dtype)

# this is used to make an array or matrix of all elements as zero
zeroes = np.zeros((3,3))
print(zeroes)

# this is used to get all the numbers starting from zero to the entered range
RR = np.arange(5)
print(RR)

# this is used to get the elements or numbers (lower limit, upper limit, differnece)
# this gives us the number in equal divisions between the limits
# the differnece is same between all the numbers
lnspc = np.linspace(1,9,9)
print(lnspc)
 
# this gives us an empty array
emp = np.empty((4,4))
print(emp)

# idnetity is used to get an identitic matrix
eg = np.identity(5)
print(eg)