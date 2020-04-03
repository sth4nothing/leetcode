class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return int(''.join('0' if '0' in bits else '1' for bits in zip(*map('{:032b}'.format, range(m, n + 1)))), 2)


class Solution2(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0xffffffff
        for num in range(m, n + 1):
            res &= num
            if res == 0:
                return 0
        return res
