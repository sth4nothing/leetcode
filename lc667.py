class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        l, r, res = 2, n, [1]
        for _ in range(k - 1):
            if len(res) & 1:
                res.append(r)
                r -= 1
            else:
                res.append(l)
                l += 1
        if len(res) & 1:
            res.extend(range(l, r + 1))
        else:
            res.extend(range(r, l - 1, -1))
        return res
