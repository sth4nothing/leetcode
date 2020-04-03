class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num, cnt = None, 0
        for n in nums:
            if n == num:
                cnt += 1
            elif cnt == 0:
                num, cnt = n, 1
            else:
                cnt -= 1
        return num
