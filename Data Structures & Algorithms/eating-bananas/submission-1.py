class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mk = max(piles)
        sk = 1
        
        while sk <= mk:
            mid = (sk + mk) // 2
            m = 0
            for i in piles:
                m += (i + mid - 1) // mid
            if m <= h:
                mk = mid - 1
            else:
                sk = mid + 1
        
        return sk