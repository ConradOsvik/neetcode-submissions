import math
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r"\w"
        string = "".join(re.findall(r"\w", s))

        for i in range(math.floor(len(string))):
            left = string[i].lower()
            right = string[len(string) - 1 - i].lower()

            if left != right:
                return False

        return True