class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2
        if mid > 1:
            for k, t in enumerate(zip(nums[mid:], nums[:mid])):
                nums[2 * k] = t[0]
                nums[1 + 2 * k] = t[1]
        return nums


class Solution2(object):
    def wiggleSort(self, nums):
        for i, num in enumerate(sorted(nums, reverse=True)):
            nums[(1 + 2 * i) % (len(nums) | 1)] = num
        return nums
