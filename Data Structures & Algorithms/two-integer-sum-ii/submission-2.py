class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            num = numbers[i]
            need = target - num
            if need in seen:
                return [seen[need] + 1, i + 1]
            seen[num] = i