# 2042. Check if Numbers Are Ascending in a Sentence


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        c = []
        for i in s.split():
            if i.isdigit():
                c.append(int(i))
    
    # Check if the list 'c' is sorted
        return c == sorted(c) and len(set(c)) == len(c)