
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Take the first string as the reference
        first_word = strs[0]
        
        for i in range(len(first_word)):
            char = first_word[i]
            
            # Check this character against the same index in all other strings
            for j in range(1, len(strs)):
                # If the current word is shorter than 'i' OR the characters don't match
                if i == len(strs[j]) or strs[j][i] != char:
                    # Return everything from the first word up to (but not including) 'i'
                    return first_word[:i]
                    
        return first_word
