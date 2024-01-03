# 28. Find the Index of the First Occurrence in a String


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       
        return haystack.find(needle)

        #another way to solve the problem
        
        # a, b = len(haystack), len(needle)

        # for i in range(a - b + 1):
        #     if haystack[i:i + b] == needle:
        #         return i

        # return -1
        