class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-(p[0]**2 + p[1]**2), p[0], p[1]) for p in points]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        return [[p[1], p[2]] for p in heap]