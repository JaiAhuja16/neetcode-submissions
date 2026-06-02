class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for ap1, ap2, price in flights:
            adj[ap1].append((ap2, price))
        q = deque([(0, src, 0)])
        dist = [float('inf')] * n
        dist[src] = 0
        while q:
            d, u, stops = q.popleft()
            if stops > k:
                continue
            for v, price in adj[u]:
                if dist[v] > d + price:
                    dist[v] = d + price
                    q.append((d + price, v, stops + 1))
        # print(dist)
        return dist[dst] if dist[dst] < float('inf') else -1