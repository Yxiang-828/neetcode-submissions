class Solution:
    def climbStairs(self, n: int) -> int:
        #how to climb a goddamn stairs brooooo
        #to reach n, i must climb to n-1 or n-2 -> n (1 step)
        #to reach n-1 i must climb to n-2 or n-3 -> n-1 (1 step)
        #to reach n-2, i must climb to n-3 or n-4 -> n-2 (1 step)
        #n=3, 2 1. 2 -> 1
        if n<=2:
            return n
        a,b=1,2
        for i in range(3,n+1):
            a,b=b,a+b
        return b
