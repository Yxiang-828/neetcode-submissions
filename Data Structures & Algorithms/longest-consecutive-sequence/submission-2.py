from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        freq=Counter(nums)
        n=len(freq)
        arr=sorted(freq.keys())
        cunt=1
        conseq=1
        for i in range(len(arr)-1):
            if arr[i+1]==arr[i]+1:
                cunt+=1
                conseq=max(conseq,cunt)
            else:
                cunt=1
        return conseq