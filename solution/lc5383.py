import collections
import functools
import heapq
import itertools
import queue
import re
from heapq import heapify, heappop, heappush
from typing import Any, Callable, Counter, Dict, Iterator, List, Set


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')

class Solution:
    def numOfWays(self, n: int) -> int:
        def one_2d(k):
            return divmod(k, 3)
        def two_1d(x, y):
            return x * 3 + y
        if n < 1:
            return 0
        MOD = 10**9 + 7
        ans = 0
        matrix = [[0] * 3 for _ in range(n)]
        matrix[0][0] = 0
        matrix[0][1] = 1
        return ans * 6 % MOD

s = Solution()

inputs = [
    (1, ),
    (2, ),
    (3, ),
    (7, ),
    (5000,),
    # ([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],),
]
outputs = [
    12,
    54,
    246,
    106494,
    30228214,
    # 7,
]

for i, (args, exp) in enumerate(zip(inputs, outputs)):
    assertEqual(s.numOfWays(*args), exp)
