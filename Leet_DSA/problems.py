#calculate the average temperature using list functions and loops

nums = int(input("how many days temperature?"))

total = 0
for i in range (1,nums+1):
    next = int(input("Enter the day" + str(i) +" high temperature "))
    total = total + next

avg = round(total/nums)
print(avg)

#same as above but also calculate how many days are above average temperature

nums = int(input("how many days temperature? "))
total = 0
temp=[]
for i in range (nums):
    next = int(input("Enter the day" + str(i+1) +" high temperature: "))
    temp.append(next)
    total+=temp[i]

avg = round(total/nums)
print("The average temperature of all the days is:",avg)

above = 0
for i in temp:
    if i > avg:
        above += 1
        
print(str(above) +"days are above average in the list")