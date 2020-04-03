class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        for n in nums:
            one = (one ^ n) & ~two
            two = (two ^ n) & ~one
        return one
