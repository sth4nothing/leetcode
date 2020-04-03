class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import bisect
        if not nums:
            return -1
        n = len(nums)
        k = n
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                k = i
                break
        r = (0, k) if target >= nums[0] else (k, n)
        idx = bisect.bisect_left(nums, target, *r)
        if 0 <= idx < n and nums[idx] == target:
            return idx
        return -1
