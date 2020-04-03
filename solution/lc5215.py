class Solution:
    def getMaximumGold(self, grid: 'List[List[int]]') -> int:
        d = ((1, 0), (0, 1), (-1, 0), (0, -1))
        m, n = len(grid), len(grid[0])
        visit = set()

        def dig(x: int, y: int) -> int:
            if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                sums = val = grid[x][y]
                grid[x][y] = 0
                sums += max(dig(x + dx, y + dy) for dx, dy in d)
                grid[x][y] = val
                return sums
            return 0

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i, j) in visit:
                    continue
                res = max(res, dig(i, j))
        return res


def main():
    s = Solution()
    print(s.getMaximumGold(
        [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))


if __name__ == "__main__":
    main()
