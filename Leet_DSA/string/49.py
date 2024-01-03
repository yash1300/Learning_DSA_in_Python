# 49 Group anagrams(copied gpt)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}

    # Iterate through each string in the input list
        for s in strs:
        # Sort the characters of the string and use it as a key
            sorted_s = ''.join(sorted(s))

        # If the key is not in the dictionary, create a new entry with an empty list
            if sorted_s not in anagram_groups:
                anagram_groups[sorted_s] = []

            # Append the original string to the list corresponding to the key
            anagram_groups[sorted_s].append(s)

        # Convert the values (lists of anagrams) to a list of lists
        result = list(anagram_groups.values())

        return result

        