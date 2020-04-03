class Solution(object):
    def validate(self, num, x, y):
        s = str(x + y)
        if num.startswith(s):
            n = len(s)
            if len(num) == n:
                return True
            return self.validate(num[n:], y, x + y)
        return False

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        if n < 2:
            return False
        ma = 0x7fffffff
        success = False
        for i in range(1, 11):
            for j in range(1, 11):
                if i + j > 2 * n // 3 or i > 1 and num[0] == '0' or j > 1 and num[i] == '0':
                    continue
                x, y = int(num[:i]), int(num[i:i + j])
                if x > ma or y > ma:
                    continue
                if self.validate(num[i + j:], x, y):
                    success = True
                    break
            if success:
                break
        return success
