class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        l = len(nums)
        used = [False] * l
        
        def backtrack():
            if len(path) == l:
                result.append(path.copy())
                return

            for i in range(l):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack()

                path.pop()
                used[i] = False

        backtrack()

        return result