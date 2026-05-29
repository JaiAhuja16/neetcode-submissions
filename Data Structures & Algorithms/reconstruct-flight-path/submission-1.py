class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        count = defaultdict(int)
        for ap1, ap2 in tickets:
            adj[ap1].append(ap2)
            count[ap1] += 1
        op = []
        for i, j in adj.items():
            j.sort(reverse = True)
        def dfs(ap):
            while adj[ap]:
                dfs(adj[ap].pop())
            op.append(ap)
        dfs("JFK")
        return op[::-1]