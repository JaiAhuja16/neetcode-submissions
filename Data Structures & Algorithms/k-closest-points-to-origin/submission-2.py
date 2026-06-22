class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, (x, y) in enumerate(points):
            heap.append((x ** 2 + y ** 2, i))
        heapq.heapify(heap)
        op = []
        for _ in range(k):
            __, i = heapq.heappop(heap)
            op.append(points[i])
        return op