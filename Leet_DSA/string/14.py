# 14. Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        strs.sort()

  
        first_string = strs[0]
        last_string = strs[-1]

        common_prefix = ""


        for i in range(len(first_string)):
            if first_string[i] == last_string[i]:
                common_prefix += first_string[i]
            else:
                break

        return common_prefix