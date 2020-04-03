class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        import collections
        d = collections.defaultdict(list)
        visited = [0] * numCourses
        for u, v in prerequisites:
            d[u].append(v)
        res = []

        def dfs(u):
            if not visited[u]:
                visited[u] = 1
                if all(dfs(v) for v in d[u]):
                    res.append(u)
                    visited[u] = 2
            return visited[u] == 2
        return res if all(dfs(k) for k in range(numCourses)) else []
