import collections
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        if m != n:
            return -1
        if n == 0:
            return 0
        diff = [i for i in range(n) if s1[i] != s2[i]]
        if len(diff) == 0:
            return 0
        if len(diff) % 2 != 0:
            return -1
        x, y = 0, 0
        for i in diff:
            if s1[i] == 'x':
                x += 1
            else:
                y += 1
        if x < y:
            x, y = y, x
        return x // 2 + y // 2 + (0 if y % 2 == 0 else 2)


s = Solution()
print(s.minimumSwap('xy', 'xy'))
