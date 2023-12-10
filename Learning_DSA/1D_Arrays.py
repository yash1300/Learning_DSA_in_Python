from array import *

#1 create an array and traverse

arr_1 = array('i',[1,43,3,6,8,9])
print(arr_1)
for i in arr_1:
    print(i)

#2 Access individual elements through indexes
print("task 2")
print(arr_1[3])

#3  append value in array using append() function
#this is used to add the valur at the end of an array
print('task 3')
arr_1.append(67)
print(arr_1)

#4 insert value in array using insert function
#to add value in between array (index position,value)
print("task 4")
arr_1.insert(2,45)
print(arr_1)

#5 extend the array using extend() function
print("task 5")
arr_2 = array('i',[4,5,6,7,8,1])
arr_2.extend(arr_1)
print(arr_2)

#6 add elemets from list using fromlist() function
#this is used to add the list in an array
print("task 6")
list_1 = [34,56,7,890]
arr_2.fromlist(list_1)
print(arr_2)

#7 remove an array element using remove() function
print("task 7")
arr_3 = array('i',[4,5,6,7,8,1])
print(arr_3)
arr_3.remove(1)
print(arr_3)

#8 pop()
print("task 8")
arr_3.pop()
print(arr_3)

#9 index()
print("task 9")
print(arr_3.index(6))

#10 reverse() to reverse an array
print("task 10")
arr_3.reverse()
print(arr_3)

#11 buffer_info() gives the position of the elements and no. of elements
print("task 11")
print(arr_3.buffer_info())

#12 count() to check the number of occurences
print("task 12")
arr_2 = array('i',[4,5,6,5,5,57,8,1])
print(arr_2.count(5))

#13 convert array to string using tostring()/tobytes() method
print("task 13")
str = arr_2.tobytes()
print(str)
arr = array('i')
arr.frombytes(str) #frombytes() is used to append a string to the array
print(arr)

#14 array to lisst using tolist() method
print("task 14")
print(arr_2.tolist())


#15 slice elements from array
print("task 15")
sui_arr = array('i',[4,5,6,5,5,57,8,1])
print(sui_arr[1:3])