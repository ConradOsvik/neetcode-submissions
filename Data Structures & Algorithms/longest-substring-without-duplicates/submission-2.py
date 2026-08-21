class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_length = 0

        for right in range(len(s)):
            right_char = s[right]

            while left < right and right_char in seen:
                left_char = s[left]
                seen.remove(left_char)
                left += 1

            if right_char not in seen:
                seen.add(right_char)
            
            if (right - left) + 1 > max_length:
                max_length = (right - left) + 1

            right += 1

        return max_length