class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        num = [[None, 0], [None, 0]]
        for n in nums:
            if n == num[0][0]:
                num[0][1] += 1
            elif n == num[1][0]:
                num[1][1] += 1
            elif num[0][1] == 0:
                num[0] = [n, 1]
            elif num[1][1] == 0:
                num[1] = [n, 1]
            else:
                num[0][1] -= 1
                num[1][1] -= 1
        return [k for k, v in num if nums.count(k) > n // 3]
