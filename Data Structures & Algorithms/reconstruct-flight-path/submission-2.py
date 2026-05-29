class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for ap1, ap2 in tickets:
            heapq.heappush(adj[ap1], ap2)
        op = []
        def dfs(ap):
            while adj[ap]:
                dfs(heapq.heappop(adj[ap]))
            op.append(ap)
        dfs("JFK")
        return op[::-1]