class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        
        def backtrack(n):
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(n)):
                path.append(n[i])
                new = n.copy()
                new.remove(n[i])
                backtrack(new)
                path.pop()

        backtrack(nums)

        return result