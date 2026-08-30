class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s) -> bool:
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        def backtrack(start, i, path):
            if start == len(s):
                result.append(path.copy())
                return

            if i == len(s):
                return

            word = s[start:i+1]

            if isPalindrome(word):
                path.append(word)
                backtrack(i + 1, i + 1, path)
                path.pop()

            backtrack(start, i + 1, path)

        backtrack(0, 0, [])
        return result