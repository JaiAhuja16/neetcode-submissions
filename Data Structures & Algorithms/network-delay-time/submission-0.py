class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in times:
            u -= 1
            v -= 1
            adj[u].append((v, w))
        times = [float('inf')] * n
        times[k - 1] = 0
        heap = [(0, k - 1)]
        while heap:
            t, u = heapq.heappop(heap)
            if t > times[u]:
                continue
            for v, w in adj[u]:
                if times[v] > t + w:
                    times[v] = t + w
                    heapq.heappush(heap, (t + w, v))
        print(*times)
        return max(times) if max(times) != float('inf') else -1