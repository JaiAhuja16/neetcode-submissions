class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(u, v):
            x1, y1 = points[u]
            x2, y2 = points[v]
            return abs(x1 - x2) + abs(y1 - y2)
        n = len(points)
        visited = [0] * n
        q = [(0, 0)]
        doori = defaultdict(lambda : float('inf'))
        s = 0
        while q:
            # print(q)
            d, u = heapq.heappop(q)
            if visited[u]:
                continue
            s += d
            visited[u] = 1
            for i in range(n):
                if not visited[i]:
                    dd = dist(u, i)
                    if dd < doori[i]:
                        doori[i] = dd
                        heapq.heappush(q, (dd, i))
        return s