class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_count = 0
        out = 0

        for right in range(len(s)):
            right_val = s[right]
            count[right_val] = count.get(right_val, 0) + 1
            max_count = max(max_count, count[right_val])

            while left < right and right - left + 1 - max_count > k:
                left_val = s[left]
                count[left_val] -= 1
                left += 1

                max_count = max(max_count, count[right_val])

            if out < sum(count.values()):
                out = sum(count.values())

        return out