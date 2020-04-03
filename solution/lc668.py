class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        low, high = 1, m * n + 1
        while low < high:
            mid = (high + low) // 2
            c = sum(min(mid // i, n) for i in range(1, m + 1))
            if c >= k:
                high = mid
            else:
                low = mid + 1
        return high
