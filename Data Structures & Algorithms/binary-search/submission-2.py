class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <=  high:
            middle = (low + high) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] > target:
                high = middle - 1
                continue

            if nums[middle] < target:
                low = middle + 1
                continue
            
        return -1