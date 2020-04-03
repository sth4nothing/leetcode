class Solution:
    def solve(self, m, *args):
        if m == self.n:
            self.res.append(
                list(('.' * v + 'Q' + '.' * (self.n - v - 1)) for v in args))
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

    def solveNQueens(self, n: int) -> 'List[List[str]]':
        self.n = n
        self.res = []
        self.solve(0, *range(self.n))
        return self.res


def main():
    s = Solution()
    print(s.solveNQueens(5))


if __name__ == "__main__":
    main()
