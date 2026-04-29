class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        right=0
        l=list(s2)
        abc=list(s1)
        while left <= len(l) - len(s1):
            if l[left] not in abc:
                left += 1
            else:
                right = left
                while len(abc) > 0 and right < len(l):
                    if l[right] in abc:
                        abc.remove(l[right])
                        right += 1
                    else:
                        if l[right] not in list(s1):
                            left = right + 1  # skip past the bad char
                        else:
                            left += 1          # char is in s1, nudge left by 1
                        abc = list(s1)         # always reset
                        break 
                if len(abc) == 0:
                    return True
                    abc = list(s1)
                    left += 1
                    left = right    # ✓ advance left so outer loop doesn't stall
        return False