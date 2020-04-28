# encoding: utf-8
'''力扣解决方案'''
import bisect
import collections
import functools
import heapq
import itertools
import json
import math
import queue
import re
from typing import (Any, Callable, Counter, DefaultDict, Dict, Iterable, List,
                    Set, Tuple)


def assert_equal(x: Any, eq: Any):
    if x == eq:
        print(f'⭕\t{x}=={eq}')
    else:
        print(f'❌\t{x}!={eq}')


data: Dict[str, List[Any]] = json.loads('''
{"inputs":[[[1,2,3,4,5,6,1],3],[[2,2,2],2],[[9,7,7,9,7,7,9],7],[[1,1000,1],1],[[1,79,80,1,1,1,200,1],3]],"outputs":[12,4,55,1,202]}
''')


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        sums = sum(cardPoints)
        if n == k:
            return sums
        ans = 0
        for i in range(k + 1):
            if i == 0:
                sums = sum(cardPoints[-k:])
            else:
                sums += cardPoints[i - 1] - cardPoints[-k - 1 + i]
            ans = max(ans, sums)
        return ans


s = Solution()
for args, eq in zip(data['inputs'], data['outputs']):
    assert_equal(s.maxScore(*args), eq)
