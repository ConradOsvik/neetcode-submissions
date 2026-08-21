import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if self.canEat(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def canEat(self, piles, h, k):
        time = 0

        for pile in piles:
            time += math.ceil(pile / k)

        return time <= h