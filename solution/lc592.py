def gcd(a, b):
    if b == 0:
        return a
    while a % b != 0:
        a, b = b, a % b
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


class fraction(object):
    def __init__(self, x, y):
        self.x = -abs(x) if x * y < 0 else abs(x)
        self.y = abs(y)
        g = gcd(abs(self.x), self.y)
        self.x //= g
        self.y //= g

    def __add__(self, f):
        return fraction(self.x * f.y + self.y * f.x, self.y * f.y)

    def __sub__(self, f):
        return fraction(self.x * f.y - self.y * f.x, self.y * f.y)

    def __repr__(self):
        return '{}/{}'.format(self.x, self.y)

    @classmethod
    def fromstring(cls, string, start=0):
        mid = string.index('/', start)
        end = mid + 1
        isnum = False
        while end < len(string):
            if isnum and not '0' <= string[end] <= '9':
                break
            if '0' <= string[end] <= '9':
                isnum = True
            end += 1
        return cls(int(string[start:mid]), int(string[mid + 1:end])), end


class Solution(object):
    def fractionAddition(self, expr):
        """
        :type expression: str
        :rtype: str
        """
        import operator
        op = {'+': operator.add, '-': operator.sub}
        isnum = True
        k, n = 0, len(expr)
        res = lastop = None
        while k < n:
            if isnum:
                fract, k = fraction.fromstring(expr, k)
                if res and lastop:
                    res = op[lastop](res, fract)
                else:
                    res = fract
                isnum = False
            else:
                lastop = expr[k]
                k += 1
                isnum = True
        return res.__repr__()
