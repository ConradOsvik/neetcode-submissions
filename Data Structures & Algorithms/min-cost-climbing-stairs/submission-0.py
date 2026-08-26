class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[-1]

        cost.append(0)

        computed = [0] * len(cost)
        computed[0] = cost[0]
        computed[1] = cost[1]

        for i in range(2, len(cost)):
            computed[i] = cost[i] + min(computed[i-1], computed[i-2])

        return computed[-1]