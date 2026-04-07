class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashy={}
        max_k=[]
        max_f=0
        for num in nums:
            if num not in hashy:
                hashy[num]= 1
                continue
            hashy[num]+=1
        sorted_keys = sorted(hashy, key=lambda x: hashy[x], reverse=True)
        return sorted_keys[:k]
        