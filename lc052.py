class Solution:
    def solve(self, m, *args):
        if m == self.n:
            self.res += 1
            return
        for i in args[m:]:
            err = False
            for j, c in enumerate(args[:m]):
                if abs(i - c) == m - j:
                    err = True
                    break
            if err:
                continue
            self.solve(m + 1, *args[:m], i, *(v for v in args[m:] if v != i))

    def totalNQueens(self, n: int) -> int:
        self.n = n
        self.res = 0
        self.solve(0, *range(self.n))
        return self.res


def main():
    s = Solution()
    for i in range(4, 10):
        print(i, s.totalNQueens(i))


if __name__ == "__main__":
    main()
