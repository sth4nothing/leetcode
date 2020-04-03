class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        nums = [nums[i] + i for i in range(n)]
        k = 0
        res = 0
        while True:
            res += 1
            if nums[k] >= n - 1:
                break
            k = max(range(nums[k], k, -1), key=lambda x: nums[x])
        return res
