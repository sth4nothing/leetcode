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
{"inputs":[[[-3,2,-3,4,2]],[[1,2]],[[1,-2,-3]]],"outputs":[5,1,5]}
''')


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 1
        sums = 0
        for v in nums:
            sums += v
            if sums + ans <= 0:
                ans += (1 - sums - ans)
        return ans


s = Solution()
for args, eq in zip(data['inputs'], data['outputs']):
    assert_equal(s.minStartValue(*args), eq)
