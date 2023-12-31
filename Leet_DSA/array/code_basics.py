# Code basics - Practice question for array

# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
# link to the practice questions

# Q1
print('Question 1 answers')

mon_ex = [2200, 2350, 2600, 2130, 2190]
print(mon_ex[1] - mon_ex[0])

print('total expense of the first quarter of the year',mon_ex[0]+mon_ex[1]+mon_ex[2])

print(2000 in mon_ex)

mon_ex.insert(5,1980)
print(mon_ex)

mon_ex[3] = mon_ex[3] - 200
print(mon_ex)

print('---------------------------------------------------------------------------')

# Q2
print('Question 2 answers')

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append('black panther')
print(heros)

heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)

heros[1:3] = ['doctor strange']
print(heros)

heros.sort()
print(heros)

print('---------------------------------------------------------------------------')

# Q3
num = int(input('Enter the upper limit: '))
arr = []
for i in range (1,num):
    if i%2 == 1:
        arr.append(i)

print('odd numbers: ',arr)