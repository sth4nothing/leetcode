import bisect
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        cp = sorted(nums)
        arr = [0] * (n + 1)
        res = []

        def search(k):
            s = 0
            while k > 0:
                s += arr[k]
                k -= (k & -k)
            return s

        def insert(k):
            while k <= n:
                arr[k] += 1
                k += (k & -k)
        for i in range(n - 1, -1, -1):
            idx = bisect.bisect_left(cp, nums[i])
            res.append(search(idx))
            insert(idx + 1)
        return res[::-1]
