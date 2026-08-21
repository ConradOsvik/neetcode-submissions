class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        maps = []
        result = []

        for st in strs:
            chars = {}

            for char in st:
                chars[char] = chars.get(char, 0) + 1

            if not maps:
                maps.append(chars)
                result.append([st])
                continue

            found_index = -1
            for i in range(len(maps)):
                if maps[i] == chars:
                    found_index = i
                    break

            if found_index != -1:
                result[found_index].append(st)
            else:
                maps.append(chars)
                result.append([st])

        return result