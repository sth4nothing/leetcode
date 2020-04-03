class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # import itertools
        # return list(set(it for x in range(2, len(nums) + 1) for it in itertools.combinations(nums, x)))
        def dfs(k):
            if k >= len(nums):
                yield []
            else:
                for arr in dfs(k + 1):
                    yield arr
                    if not arr or nums[k] <= arr[0]:
                        yield [nums[k]] + arr
        return list(arr for arr in dfs(0) if len(arr) > 1)
