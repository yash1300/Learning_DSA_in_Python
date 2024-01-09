# 32. Longest Valid Parentheses
# i also thought the same approach but wasnt able to convert it to the code 



class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]  # Initialize with a start index

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # If popped -1, add a new start index
                else:
                    # Update the length of the valid substring
                    max_length = max(max_length, i - stack[-1])

        return max_length
