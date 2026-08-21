class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        max_time = -1
        result = 0

        data = sorted(zip(position, speed))

        for dt in reversed(data):
            pos = dt[0]
            sp = dt[1]
            time = (target - pos) / sp

            print(dt, time)

            if max_time < 0:
                max_time = time
                result += 1
                continue

            if max_time < time:
                max_time = time
                result += 1

        return result

        # for i in range(len(data)):
        #     pos = data[i][0]
        #     sp = data[i][1]
        #     time = (target - pos) / sp

        #     print(time)

        #     if not stack:
        #         stack.append(time)
        #         result += 1
        #         continue

        #     top = stack.pop()
        #     if top <= time:
        #         stack.append(time)
        #     else:
        #         stack.append(time)
        #         result += 1

        return result