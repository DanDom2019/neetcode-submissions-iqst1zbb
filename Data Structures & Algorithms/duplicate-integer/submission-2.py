class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        disc={}
        for num in nums:
            if num not in disc.keys():
                disc[num]=1
            else:
                disc[num]+=1
        for value in disc.values():
            if value >1:
                return True
        return False
        