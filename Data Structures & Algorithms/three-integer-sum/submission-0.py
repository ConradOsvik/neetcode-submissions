class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(nums)):
            val1 = nums[i]
            seen = set()
            for j in range(len(nums)):
                if i == j:
                    continue

                val2 = nums[j]
                target = -(val1 + val2)

                if target in seen:
                    sol = [val1, val2, target]
                    sol.sort()
                    if sol not in ans:
                        ans.append(sol)

                seen.add(val2)

        return ans
