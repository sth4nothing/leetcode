# -*- coding:utf-8 -*-
# 力扣解决方案
import bisect
import collections
import functools
import heapq
import itertools
import json
import math
import queue
import re
from typing import (Any, Callable, Counter, DefaultDict, Dict, Iterable,
                    Iterator, List, Optional, Sequence, Set, Tuple, TypeVar)

import my_timer


@my_timer.timer_wrap
def assert_equal(fn: Callable, args: Sequence[Any], exp: Any):
    x = fn(*args)
    if x == exp:
        print(f'⭕\t{x}=={exp}')
    else:
        print(f'❌\t{x}!={exp}')


data = json.loads('''
{"inputs":[[2,3,1],[5,2,3],[9,1,1],[50,100,25],[37,17,7]],"outputs":[6,0,1,34549172,418930126]}
''')

MOD = 10**9 + 7


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k > m or k > n:
            return 0
        if n == k:
            return math.factorial(m) // math.factorial(n) // math.factorial(
                m - n) % MOD
        dp = [[[-1] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        def f(n, m, k):
            if k > m or k > n:
                return 0
            if n == k:
                return math.factorial(m) // math.factorial(
                    n) // math.factorial(m - n) % MOD
            if k == 0 or n == 0 or m == 0:
                return 0
            return sum(g(n, i, k) for i in range(k, m + 1)) % MOD

        def g(n, m, k):
            if k > m or k > n:
                return 0
            if n == k:
                return math.factorial(m - 1) // math.factorial(
                    n - 1) // math.factorial(m - n) % MOD
            if k == 0 or n == 0 or m == 0:
                return 0
            if dp[n][m][k] == -1:
                dp[n][m][k] = (m * g(n - 1, m, k) +
                               f(n - 1, m - 1, k - 1)) % MOD
            return dp[n][m][k]

        return f(n, m, k)


s = Solution()

for i, (args, exp) in enumerate(zip(data['inputs'], data['outputs'])):
    assert_equal(s.numOfArrays, args, exp)
