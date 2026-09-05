class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        maxwata=0
        while left<right:
            maxwata=max(maxwata,(right-left)*min(heights[right],heights[left]))
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return maxwata
            
            