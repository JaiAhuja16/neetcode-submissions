class Solution:
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        inD = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            inD[course] += 1
        q = deque(i for i in range(numCourses) if inD[i] == 0)
        taken = 0
        while q:
            u = q.popleft()
            taken += 1
            for v in adj[u]:
                inD[v] -= 1
                if inD[v] == 0:
                    q.append(v)
        return taken == numCourses