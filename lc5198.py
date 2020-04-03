class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        a, b, c = sorted((a, b, c))

        def gcd(x, y):
            if x > y:
                x, y = y, x
            z = y % x
            if z == 0:
                return x
            return gcd(z, x)

        def lcm(x, y):
            return x * y // gcd(x, y)
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, ac)

        def rank(x):
            return x // a + x // b + x // c - x // ab - x // ac - x // bc + x // abc
        r = a * n + 1
        l = a * (2 * n - rank(r))
        while True:
            m = (l + r) // 2
            k = rank(m)
            if k == n:
                break
            if k < n:
                l = m
            else:
                r = m
        return max(m // a * a, m // b * b, m // c * c)


s = Solution()
print(s.nthUglyNumber(1000000000,
                      2,
                      217983653,
                      336916467))
