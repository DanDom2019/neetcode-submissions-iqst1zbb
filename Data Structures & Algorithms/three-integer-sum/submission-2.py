class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        s = sorted(nums)
        for i in range(len(s) - 2):
            if i > 0 and s[i] == s[i-1]:   # skip duplicate i
                continue
            left = i + 1
            right = len(s) - 1
            while left < right:
                total = s[i] + s[left] + s[right]
                if total < 0:
                    left += 1
                elif total == 0:
                    l.append([s[i], s[left], s[right]])
                    while left < right and s[left] == s[left+1]:   # skip dup left
                        left += 1
                    while left < right and s[right] == s[right-1]: # skip dup right
                        right -= 1
                    left += 1   # move both inward, keep searching
                    right -= 1
                else:
                    right -= 1
        return l