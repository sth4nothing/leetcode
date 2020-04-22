# -*- coding:utf-8 -*-
# 力扣解决方案
import bisect
import collections
import functools
import heapq
import itertools
import json
import queue
import re
from typing import (Any, Callable, Counter, DefaultDict, Dict, Iterable,
                    Iterator, List, Optional, Sequence, Set, Tuple, TypeVar)


def assert_equal(x: Any, eq: Any):
    if x == eq:
        print(f'⭕\t{x}=={eq}')
    else:
        print(f'❌\t{x}!={eq}')


data = json.loads('''
{"inputs":[["croakcroak"],["crcoakroak"],["croakcrook"],["croakcroa"]],"outputs":[1,2,-1,-1]}
''')


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak = "croak"
        n = len(croak)
        pos = {c: i for i, c in enumerate(croak)}
        cnt = [0] * n
        for c in croakOfFrogs:
            if c not in pos:
                return -1
            j = pos[c]
            if cnt[j]:
                cnt[j] -= 1
                cnt[(j + 1) % n] += 1
            elif j == 0:
                cnt[1] += 1
        return -1 if sum(cnt[1:]) else cnt[0]


s = Solution()

for i, (args, exp) in enumerate(zip(data['inputs'], data['outputs'])):
    assert_equal(s.minNumberOfFrogs(*args), exp)
