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

            skip = False
            i = 0
            while not skip and i < len(maps):
                mp = maps[i]

                print(st, mp, chars)

                if mp == chars:
                    result[i].append(st)
                    skip = True
                    continue
                
                i += 1

            if skip:
                continue

            maps.append(chars)
            result.append([st])

        return result