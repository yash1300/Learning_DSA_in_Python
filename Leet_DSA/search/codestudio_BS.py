# binary search in python



def search(nums: [int], target: int):
    # write your code logic !!
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
      
        if arr[mid] == target:
            return mid
     
        elif arr[mid] < target:
            low = mid + 1
       
        else:
            high = mid - 1
    return -1



    
n= int (input())
arr = list(map(int,input().strip().split()))[:n]
target =int (input())
print (search(arr, target))