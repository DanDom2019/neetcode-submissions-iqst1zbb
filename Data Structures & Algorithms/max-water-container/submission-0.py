class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxSize=0
        while left<right:
            s=self.cSize(left,right,heights)
            if s> maxSize:
                maxSize=s
            if heights[left]<=heights[right]:
                left+=1
            else:
                    right -=1
        return maxSize
        
        
    def cSize(self, left, right, heights):
        height=min(heights[left],heights[right])
        return (right-left)*height