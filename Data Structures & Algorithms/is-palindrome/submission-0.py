class Solution:
    def isPalindrome(self, s: str) -> bool:
        news=""
        for ch in s:
            if ch.isalnum():
                news+=(ch.lower())
        n=len(news)
        left=0
        right=n-1
    
        while left<right:
            if news[left]!=news[right]:
                return False
            left+=1
            right-=1
        return True