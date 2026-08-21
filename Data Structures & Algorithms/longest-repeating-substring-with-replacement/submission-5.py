class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        out = 0

        for right in range(len(s)):
            right_val = s[right]
            if right_val in count:
                count[right_val] += 1
            else:
                count[right_val] = 1

            max_key = max(count, key=lambda k: count[k])

            print(count)

            while left < right and sum(count.values()) - count[max_key] > k:
                left_val = s[left]
                count[left_val] -= 1
                left += 1

                max_key = max(count, key=lambda k: count[k])

                if out < sum(count.values()):
                    out = sum(count.values())

        if out < sum(count.values()):
            out = sum(count.values())

        return out