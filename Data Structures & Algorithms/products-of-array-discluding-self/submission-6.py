class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        n=len(nums)
        #repetition:
        #for every number im recalculating the rest's product except itself. 
        #we have to store 2 things, culmulative product of 0 to i-1 cumulative sum given that i>0, culmulative product of i+1 to n-1 given that i<n-1. and then multiply the 2 products together.
        #so we need 2 arrays. one to store n-1..n-1, n-1..n-2, n-1..0 (in reverse) so when i need i+1 say 4, ill access index 4
        #another stores 0..0,0..1,0...n-1
        cumback=deque()
        cumfront=[]
        for i in range(n):
            if i==0:
                cumfront.append(nums[0])
                cumback.append(nums[n-1])
                continue
            cumfront.append(cumfront[i-1]*nums[i])
            cumback.append(cumback[i-1]*nums[n-1-i])
        for i in range(n):
            if i==0:
                output.append(cumback[n-2])
                continue
            if i==n-1:
                output.append(cumfront[n-2])
                continue
            output.append(cumfront[i-1]*cumback[n-i-2])
        return output

        
        