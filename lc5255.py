class Solution:
    def oddCells(self, n: int, m: int, indices: 'List[List[int]]') -> int:
        matrix = [[0] * m for _ in range(n)]
        for x, y in indices:
            for i in range(m):
                matrix[x][i] += 1
            for i in range(n):
                matrix[i][y] += 1
        return sum(v % 2 for a in matrix for v in a)

s = Solution()
print(s.oddCells(2, 3, [[0,1],[1,1]]))