class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        tree = {num // 10: num % 10 for num in nums}
        self.res = 0

        def dfs(d, p, s):
            key = d * 10 + p
            if key not in tree:
                return
            s += tree[key]
            if p >= 5 or (d + 1) * 10 + 2 * p - 1 not in tree and (d + 1) * 10 + 2 * p not in tree:
                self.res += s
            else:
                dfs(d + 1, 2 * p - 1, s)
                dfs(d + 1, 2 * p, s)
        dfs(1, 1, 0)
        return self.res
