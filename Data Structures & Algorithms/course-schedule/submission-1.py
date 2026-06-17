class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [to_do, pre-requisite]
        adj = [set() for _ in range(numCourses)]
        inD = [0] * numCourses
        for to_do, prereq in prerequisites:
            adj[prereq].add(to_do)
            inD[to_do] += 1

        visited = [0] * numCourses

        def dfs(curr):
            visited[curr] = 1
            for v in adj[curr]:
                inD[v] -= 1
                if not visited[v] and inD[v] == 0:
                    dfs(v)
                    
        for v in range(numCourses):
            if inD[v] == 0 and not visited[v]:
                dfs(v)
                
        return numCourses == visited.count(1)