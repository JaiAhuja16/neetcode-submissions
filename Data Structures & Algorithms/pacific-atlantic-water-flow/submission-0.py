class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        visited_pac = set()
        visited_atl = set()

        def neighbours(i, j):
            L = []
            if i < m - 1 and heights[i + 1][j] >= heights[i][j]:
                L.append((i + 1, j))
            
            if j < n - 1 and heights[i][j + 1] >= heights[i][j]:
                L.append((i, j + 1))
            
            if i > 0 and heights[i - 1][j] >= heights[i][j]:
                L.append((i - 1, j))
            
            if j > 0 and heights[i][j - 1] >= heights[i][j]:
                L.append((i, j - 1))

            return L

        def dfs(x, y, visited):
            visited.add((x, y))
            for i, j in neighbours(x, y):
                if (i, j) in visited:
                    continue
                dfs(i, j, visited)

        for i in range(m):
            dfs(i, 0, visited_pac)
            dfs(i, n - 1, visited_atl)
        for i in range(n):
            dfs(0, i, visited_pac)
            dfs(m - 1, i, visited_atl)
        
        return list(visited_pac.intersection(visited_atl))