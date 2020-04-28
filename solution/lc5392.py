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
{
    "inputs": [
        [
            "011101"
        ],
        [
            "00111"
        ],
        [
            "1111"
        ],
        ["01001"]
    ],
    "outputs": [
        5,
        5,
        3,
        4
    ]
}
''')


class Solution:
    def maxScore(self, s: str) -> int:
        cnt = collections.Counter(s)
        zeros = cnt['0']
        ones = cnt['1']
        score = ones + 1 if s[0] == '0' else ones - 1
        ans = score
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                score += 1
            else:
                score -= 1
            ans = max(ans, score)
        return ans


s = Solution()
for args, eq in zip(data['inputs'], data['outputs']):
    assert_equal(s.maxScore(*args), eq)
