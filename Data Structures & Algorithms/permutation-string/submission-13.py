class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        win_count = [0] * 26
        
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        
        for i in range(len(s2)):
            win_count[ord(s2[i]) - ord('a')] += 1
            
            # shrink window once it exceeds len(s1)
            if i >= len(s1):
                win_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if win_count == s1_count:
                return True
        
        return False