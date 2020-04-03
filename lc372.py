def mul(x, y):
    return x * y % 1337


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if a >= 1337:
            return self.superPow(a % 1337, b)
        if a == 0 or a == 1:
            return a
        n = len(b)
        res = 1
        for i in range(0, n):
            if b[n - 1 - i]:
                res = mul(res, pow(a, b[n - 1 - i], 1337))
            a = pow(a, 10, 1337)
        return res
