class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)

        if l < 1:
            return 0

        if l < 2:
            return nums[0]

        dp = [0] * l
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, l):
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
        
        return max(dp[-1], dp[-2])