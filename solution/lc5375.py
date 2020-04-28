# encoding: utf-8
import bisect
import collections
import json
import math
import queue
import heapq
from typing import (Any, Callable, Counter, DefaultDict, Dict, Iterable, List,
                    Set, Tuple)


def assert_equal(x: Any, eq: Any):
    if x == eq:
        print(f'√\t{x}=={eq}')
    else:
        print(f'×\t{x}!={eq}')


data: Dict[str, List[Any]] = json.loads('''
{"inputs":[["1000",10000],["1000",10],["1317",2000],["2020",30],["1234567890",90]],"outputs":[1,0,8,1,34]}
''')

MOD = 10 ** 9 + 7


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0] * len(s)
        n, m = len(s), len(str(k))
        for i in reversed(range(0, n)):
            if s[i] == '0':
                continue
            for j in range(i + 1, i + m + 1):
                if j > n:
                    break
                if int(s[i:j]) <= k:
                    dp[i] += 1 if j == n else dp[j]
            dp[i] %= MOD
        return dp[0]


s = Solution()
for args, eq in zip(data['inputs'], data['outputs']):
    assert_equal(s.numberOfArrays(*args), eq)
