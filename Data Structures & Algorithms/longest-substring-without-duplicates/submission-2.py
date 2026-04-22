class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        length=0
        maxString=set()
        currentString=set()
        left=0
        right=0
        
        while right < len(s):
            if s[right] not in currentString:
                currentString.add(s[right])
                length = max(length, len(currentString))
                right += 1          # always move right forward
            else:
                currentString.remove(s[left])  # shrink from left
                left += 1
        return length
