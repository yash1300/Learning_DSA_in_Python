# 26. Remove Duplicates from Sorted Array


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
   
        for i in range(1, len(nums)):
       
            if nums[i] != nums[current]:
            
                current += 1
                nums[current] = nums[i]

        return current + 1