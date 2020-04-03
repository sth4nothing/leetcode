class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        res = []
        points = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(x, y, k):
            if not visited[x][y] or (k == 0 and visited[x][y] & 3 != 3) or visited[x][y] & k != k:
                if x == 0 or y == 0:
                    visited[x][y] |= 1
                if x == m - 1 or y == n - 1:
                    visited[x][y] |= 2
                visited[x][y] |= k
                if visited[x][y] == 3:
                    visited[x][y] |= 4
                    res.append((x, y))
                for p, q in points:
                    if 0 <= x + p < m and 0 <= y + q < n and matrix[x][y] <= matrix[x + p][y + q]:
                        dfs(x + p, y + q, visited[x][y] & 3)
        for i in range(m):
            dfs(i, 0, 0)
            dfs(i, n - 1, 0)
        for j in range(1, n - 1):
            dfs(0, j, 0)
            dfs(m - 1, j, 0)
        return res
