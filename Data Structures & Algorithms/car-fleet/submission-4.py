class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        max_time = -1
        result = 0

        data = sorted(zip(position, speed))

        for dt in reversed(data):
            pos = dt[0]
            sp = dt[1]
            time = (target - pos) / sp

            if max_time < 0:
                max_time = time
                result += 1
                continue

            if max_time < time:
                max_time = time
                result += 1

        return result