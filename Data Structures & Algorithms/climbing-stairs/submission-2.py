class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        computed = [0] * n
        computed[0] = 1
        computed[1] = 2

        for i in range(2, n):
            computed[i] = computed[i-1] + computed[i-2]
    
        return computed[-1]