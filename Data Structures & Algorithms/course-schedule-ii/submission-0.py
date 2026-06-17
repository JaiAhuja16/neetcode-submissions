class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        inD = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            inD[course] += 1
        q = deque(i for i in range(numCourses) if inD[i] == 0)
        taken = 0
        op = []
        while q:
            u = q.popleft()
            op.append(u)
            taken += 1
            for v in adj[u]:
                inD[v] -= 1
                if inD[v] == 0:
                    q.append(v)
        return op if taken == numCourses else []