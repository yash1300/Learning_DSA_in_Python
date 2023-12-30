# 35. Search Insert Position (Binary search) 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while high>=low:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                high = mid -1
            elif nums[mid] < target:
                low = mid + 1
        if nums[mid]>target:
            return mid
        return mid+1