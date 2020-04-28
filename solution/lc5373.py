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
{"inputs":[[7],[10],[19]],"outputs":[2,2,3]}
''')


fib = [1, 1]
while True:
    x = fib[-2] + fib[-1]
    if x > 0x7fffffff:
        break
    fib.append(x)

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def findClosestFibNum(num):
            i = bisect.bisect(fib, num) - 1
            return fib[i]
        ans = 0
        while k > 0:
            k -= findClosestFibNum(k)
            ans += 1
        return ans


s = Solution()
for args, eq in zip(data['inputs'], data['outputs']):
    assert_equal(s.findMinFibonacciNumbers(*args), eq)
