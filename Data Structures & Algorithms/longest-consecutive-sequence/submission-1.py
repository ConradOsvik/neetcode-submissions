class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()        

        prev = None
        count = 1
        current = 1

        print(nums)
        for i in range(len(nums)):
            num = nums[i]

            if num == prev:
                prev = num
                continue
            elif num - 1 == prev:
                current += 1
            else:
                if current > count:
                    count = current
                current = 1

            prev = num

        if current > count:
            count = current

        return count