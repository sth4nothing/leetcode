class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        from functools import reduce
        if num < 10:
            return num
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        n = len(digits)
        for i in range(n - 2, - 1, -1):
            if digits[i] > digits[i + 1]:
                j, k = max(range(0, i + 1), key=lambda x: digits[x]), i + 1
                while k < n and digits[j] > digits[k]:
                    k += 1
                digits[j], digits[k - 1] = digits[k - 1], digits[j]
                break
        return reduce((lambda p, q: p * 10 + q), reversed(digits), 0)
