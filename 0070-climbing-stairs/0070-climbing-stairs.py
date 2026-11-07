class Solution(object):
    def climbStairs(self, n):
        """:type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        prev1 = 2  # ways to reach n-1
        prev2 = 1  # ways to reach n-2
        current = 0
        
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return current