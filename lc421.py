class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(31, -1, -1):
            res <<= 1
            pre = {num >> i for num in nums}
            res += any(res ^ 1 ^ p in pre for p in pre)
        return res
