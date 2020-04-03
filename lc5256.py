class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: 'List[int]') -> 'List[List[int]]':
        if sum(colsum) != upper + lower:
            return []
        n = len(colsum)
        res = [[0] * n for _ in range(2)]
        def solve(k, u, l):
            if u < 0 or l < 0:
                return False
            if k == n:
                return u == 0 and l == 0
            if colsum[k] == 0:
                res[0][k] = 0
                res[1][k] = 0
                return solve(k + 1, u, l)
            if colsum[k] == 2:
                res[0][k] = 1
                res[1][k] = 1
                return solve(k + 1, u - 1, l - 1)
            res[0][k] = 1
            res[1][k] = 0
            if solve(k + 1, u - 1, l):
                return True
            res[0][k] = 0
            res[1][k] = 1
            return solve(k + 1, u, l - 1)
        if solve(0, upper, lower):
            return res
        return []


s = Solution()
print(s.reconstructMatrix(99,
                          102,
                          [2,1,1,1,1,2,0,2,2,2,0,1,0,0,2,1,1,1,2,2,1,2,1,1,1,1,2,0,1,2,1,1,2,2,1,0,2,0,1,0,0,1,0,1,0,1,2,1,0,1,1,0,2,1,1,0,1,0,1,0,1,0,1,1,2,1,1,2,2,1,1,2,2,2,0,1,1,0,0,1,1,1,1,0,0,2,1,1,1,2,1,1,2,1,0,1,2,0,1,1,2,2,2,1,1,2,2,2,0,2,1,2,2,1,0,1,1,1,1,0,1,1,1,2,0,1,0,2,1,2,1,1,2,1,1,2,1,1,1,1,0,2,0,1,0,0,1,1,1,0,1,1,0,0,2,0,0,1,1,1,0,0,2,2,1,1,1,1,1,1,0,2,1,1,0,1,2,1,2,0,1,0,1,1,1,0,1,1,0,0,0,0,1,2,2,2,1,1,0,2]))
