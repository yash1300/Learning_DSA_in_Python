#This file is created just to practice the python concepts

from collections import Counter
#counter is used to record the counts of all the character present in the string
print("hello python")

# suppose we have a string 
my_str = "aaaaabbbbrbrbrbraaabiiiiii"
my_counter = Counter(my_str)
print(my_counter)

print(my_counter.most_common())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.update())
print(my_counter.items())
print(my_counter.popitem())

