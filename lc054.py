class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        direct = 0
        d = (1, -1)
        pos = [0, -1]
        m, n = len(matrix), len(matrix[0])
        while True:
            l, r = divmod(direct, 4)
            b = ((l, n - l - 1), (l + 1, m - l - 1), (l, n - l - 2), (l + 1, m - l - 2))
            if not b[r][0] <= pos[1 - r % 2] + d[r // 2] <= b[r][1]:
                break
            while b[r][0] <= pos[1 - r % 2] + d[r // 2] <= b[r][1]:
                pos[1 - r % 2] += d[r // 2]
                res.append(matrix[pos[0]][pos[1]])
            direct += 1
        return res
