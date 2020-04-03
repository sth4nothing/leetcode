

class Solution:
    def closedIsland(self, grid: 'List[List[int]]') -> int:
        m, n = len(grid), len(grid[0])
        matrix = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(m + 2):
            for j in range(n + 2):
                if i == 0 or i == m + 1 or j == 0 or j == n + 1:
                    matrix[i][j] = -1
                else:
                    matrix[i][j] = grid[i - 1][j - 1]
        d = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        )

        def close_island(x, y):
            if matrix[x][y] == -1:
                return 1
            if matrix[x][y] == 0:
                matrix[x][y] = 1
                return sum(close_island(x + dx, y + dy) for dx, dy in d)
            return 0
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i][j] == 0 and close_island(i, j) == 0:
                    res += 1
        return res


s = Solution()
print(s.closedIsland([[1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 1, 1]]))
