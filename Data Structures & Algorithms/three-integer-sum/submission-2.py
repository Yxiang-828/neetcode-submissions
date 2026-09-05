class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m=len(nums)
        numset={}
        for i in range(m):
            if nums[i] not in numset:
                numset[nums[i]]=set()
            numset[nums[i]].add(i)
        
        ans=[]
        for i in range(m):
            for j in range(m):
                bruh=-(nums[i]+nums[j]) 
                if i!=j and bruh in numset and any(id!=i and id!=j for id in numset[bruh]):
                    candidate=sorted([nums[i],nums[j],-(nums[i]+nums[j])])
                    if candidate not in ans:
                        ans.append(candidate)
        return ans