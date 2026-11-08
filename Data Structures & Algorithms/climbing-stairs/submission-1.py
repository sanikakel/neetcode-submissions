class Solution:
    def climbStairs(self, n: int) -> int:
        # n represents the number of steps to reach the top of the staircase
        # you can advance either 1 or 2 steps at a time
        # return the number of distinct ways to climb the top of the staircase
        # n=1: 1
        # n=2: 1+1, 2
        # n=3: 1+1+1, 1+2, 2+1
        # n=4: 1+1+1+1, 1+2+1, 1+1+2, 2+1+1, 2+2
        # n=5: 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 2+2+1, 2+1+2, 1+2+2

        # 1, 2, 3, 5, 8...

        '''
        if n <= 2:
            return n

        return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''

        if n <= 2:
            return n

        prev, curr = 1, 2
        for i in range(3, n+1):
            prev, curr = curr, prev + curr
        return curr