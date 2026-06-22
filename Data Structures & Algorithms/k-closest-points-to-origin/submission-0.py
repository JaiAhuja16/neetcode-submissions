class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def dist(x, y):
            return (x ** 2 + y ** 2) ** 0.5
        for i, (x, y) in enumerate(points):
            heapq.heappush(heap, (dist(x, y), i))
        op = []
        for _ in range(k):
            __, i = heapq.heappop(heap)
            op.append(points[i])
        return op