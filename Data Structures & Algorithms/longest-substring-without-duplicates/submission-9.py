class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #no dupe ch
        n=len(s)
        count=0
        maxcount=0
        i=0
        sett=set()
        for j in range(n):
            while s[j] in sett:
                sett.remove(s[i])
                i+=1
            sett.add(s[j])
            maxcount=max(maxcount,j-i+1)
        return maxcount

            