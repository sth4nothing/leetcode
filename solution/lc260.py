class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        mask = 1
        while not mask & xor:
            mask <<= 1
        a, b = 0, 0
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
