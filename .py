from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a hash map to hold lists of anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters of the string to create a unique key
            sorted_key = "".join(sorted(s))
            # Append the original string to the matching key list
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())