import collections
from typing import Callable, List, Set, Any, Dict, Counter, Iterator


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


def findMatchStart(s1, s2):
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            return i
    return n


def sub(s2, s1, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(s1)
    ans = 0
    for i in range(start, end):
        ans = ans * 26 + ord(s2[i]) - ord(s1[i])
    return ans


MAX = 10**9 + 7


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        m = findMatchStart(s1, s2)
        l = len(evil)
        if m == n:
            return 0
        if evil in s1[:m]:
            return 0
        ans = sub(s2, s1, m) + 1
        if ans <= 0:
            return 0
        for i in range(min(m + 1, l)):
            if not s1[:m].endswith(evil[:i]) or l - i > n - m:
                continue
            if i == 0:
                for j in range(m, n - l + 1):
                    a = sub(s2, s1, m, j) - 1
                    if s1[j:j + l] < evil:
                        a += 1
                    elif s1[j:j + l] == evil:
                        ans -= sub(''.rjust(n - j - l, 'z'), s1[j + l:]) + 1
                    if s2[j:j + l] > evil:
                        a += 1
                    elif s2[j:j + l] == evil:
                        ans -= sub(s2[j + l:], ''.rjust(n - j - l, 'a')) + 1
                    if a <= 0:
                        continue
                    ans -= a * 26**(n - j - l)
            elif evil[i:] <= s2[m:] and evil[i:].rjust(n - m, 'a') >= s1[m:]:
                ans -= 26**(n - m - l + i)
        return ans % MAX


s = Solution()

inputs = [
    (2, 'aa', 'da', 'b'),
    (8, 'leetcode', 'leetgoes', 'leet'),
    (2, 'gx', 'gz', 'x'),
]
outputs = [
    51,
    0,
    2,
]

for i, (args, exp) in enumerate(zip(inputs, outputs)):
    assertEqual(s.findGoodStrings(*args), exp)
