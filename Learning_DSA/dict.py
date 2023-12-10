# this works in the form of key value pair 
# time = O(n)  space = O(n)


eng_hi = {'one':'ek', 'two':'do', 'three':'teen', 'four':'chaar'}
print(eng_hi['four'])

# insert and update operations
#time: O(1)  space: O(1)
eng_hi['two'] = 'don'
eng_hi['maths'] = 'ganit'
print(eng_hi)

#traverse
# time: O(n) space:O(1)
def traverse(dict):
    for key in dict:
        print(key,dict[key])
        
traverse(eng_hi)

#searching in dict

def search(dict,value):
    for key in dict:
        if value == dict[key]:
            return key,value
    return 'mandal aaple aabhari aahe'

search(eng_hi,'chaar')