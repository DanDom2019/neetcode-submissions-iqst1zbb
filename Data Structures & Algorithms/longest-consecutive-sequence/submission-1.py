import heapq
class Solution:
    def heap_sort_unique(self,nums):
        heapq.heapify(nums)
        result=[]
        while nums:
            val=heapq.heappop(nums)
            if not result or result[-1] != val:
                result.append(val)
        return result 

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        #sort it first no dulplicated
        u=self.heap_sort_unique(nums)
        #list different 1 +1, otherwise log it and start another one, output the largest
        max_longest=1
        longest=1
        for i in range(1,len(u)):
            if i ==0:
                continue
            if u[i]-u[i-1]==1:
                longest += 1
                max_longest = max(max_longest, longest)  # update inside loop
            else:
                longest=1
        return max_longest
