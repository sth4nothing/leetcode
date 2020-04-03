class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        from queue import Queue
        m, n = len(matrix), len(matrix[0])
        res = [[0] * n for _ in range(m)]
        points = ((-1, 0), (1, 0), (0, -1), (0, 1))
        que = Queue()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    que.put((i, j))
        while not que.empty():
            x, y = que.get()
            for p, q in points:
                if 0 <= x + p < m and 0 <= y + q < n and res[x + p][y + q] == 0:
                    matrix[x + p][y + q] |= 2
                    res[x + p][y + q] = res[x][y] + 1
                    que.put((x + p, y + q))
        return res
