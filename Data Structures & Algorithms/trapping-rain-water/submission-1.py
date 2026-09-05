class Solution:
    def trap(self, height: List[int]) -> int:
        #trapping logic: must have walls of >0 height and must exist walls obviously
        #trapping logic: count the pools trapped by separating by peaks.
        #trapping logic: within each pool, the water caught is min(two peaks)-curr. iter-> right
        n=len(height)
        left=0
        right=n-1
        leftmax=0
        rightmax=0
        ans=0
        while left<right:
            if height[left]<height[right]:       
                if height[left]<leftmax:
                    ans+=leftmax-height[left]
                else:
                    leftmax=height[left]
                left+=1
            else:
                if height[right]<rightmax:
                    ans+=rightmax-height[right]
                else:
                    
                    rightmax=height[right]
                right-=1
        return ans