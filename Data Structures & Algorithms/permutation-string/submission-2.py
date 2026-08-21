class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_size = len(s1)
        chars = {}

        matches = 0

        for char in s1:
            chars[char] = chars.get(char, 0) + 1

        for left in range(-window_size, len(s2)):
            right = left + window_size

            if left >= 0:
                left_char = s2[left]
                if left_char in chars:
                    if chars[left_char] == 0:
                        matches -= 1
                    chars[left_char] += 1

            if right < len(s2):
                right_char = s2[right]
                if right_char in chars:
                    chars[right_char] -= 1
                    if chars[right_char] == 0:
                        matches += 1

            if matches == len(chars):
                return True

        return False