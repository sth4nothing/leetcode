class Solution:
    def solveM(self, k, n, r):
        s, e = 0, n
        while True:
            if e - s <= 1:
                return s
            mid = (s + e) // 2
            d = r - (mid + 1) * mid // 2 - k * n * mid
            if d == 0:
                return mid
            if d < 0:
                e = mid
            else:
                s = mid

    def distributeCandies(self, c: int, n: int) -> 'List[int]':
        k = ((2 * c + 0.25) ** 0.5 - 0.5) // n
        r0 = c - (n * k + 1) * n * k // 2
        m = 0 if r0 == 0 else self.solveM(k, n, r0)
        r1 = r0 - (m + 1) * m // 2 - k * n * m
        res = []
        for i in range(1, n + 1):
            K = k if i > m else k + 1
            res.append(int((K - 1) * K * n // 2 + i *
                           K + (0 if i != m + 1 else r1)))
        return res


def main():
    s = Solution()
    print(s.distributeCandies(10, 3))


if __name__ == "__main__":
    main()
