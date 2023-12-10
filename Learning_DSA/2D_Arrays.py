import numpy as np

# INSERTION operation in 2D array

arr_2D = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(arr_2D)
new_1 = np.insert(arr_2D,0,[[3,4,5,6]],axis=1)
print(new_1)
new_2 = np.insert(arr_2D,0,[[3,4,5,6]],axis = 0)
print(new_2)


# access elements in 2D array
print("step 2")
def accessElements(array,rowIndex,colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Invalid Index")
    else:
        print(array[rowIndex][colIndex])

accessElements(arr_2D,2,2)


#3 TRAVERSAL in 2D array

print("step 3")
def traveler(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traveler(arr_2D)

#4 SEARCHING in 2D array


print("step 4")
def searchingin2D(array,target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return 'The value is located at index ' + str(i) + "x" + str(j)
    return"chal bhosadike"

print(searchingin2D(arr_2D,10))


#5 DELETION in 2D array

print("step 5")
tamtam = np.delete(arr_2D,0,axis = 0) # 0 for row and 1 for column
print(tamtam)