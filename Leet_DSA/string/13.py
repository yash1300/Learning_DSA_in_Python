# 13. Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary to map Roman numerals to their corresponding values
        roman_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Initialize a variable to store the resulting integer
        num = 0
        
        # Iterate through each character in the input string 's'
        for i in range(len(s)):
            # Check if the current Roman numeral is greater than the one before it
            if i > 0 and roman_list[s[i]] > roman_list[s[i - 1]]:
                # If true, subtract twice the value of the previous numeral
                num += roman_list[s[i]] - 2 * roman_list[s[i - 1]]
            else:
                # Otherwise, add the value of the current numeral to the result
                num += roman_list[s[i]]

        # Return the final integer result
        return num