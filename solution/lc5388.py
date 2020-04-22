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
{"inputs":[["a0b1c2"],["leetcode"],["1229857369"],["covid2019"],["ab123"]],"outputs":["0a1b2c","","","c2o0v1i9d","1a2b3"]}
''')


class Solution:
    def reformat(self, s: str) -> str:
        cnt: Counter[int] = collections.Counter(map(lambda x:1 if x.isdigit() else 0, s))
        if abs(cnt[0] - cnt[1]) > 1 or len(s) == 0:
            return ''
        digit_queue: 'queue.Queue[str]' = queue.Queue()
        alpha_queue: 'queue.Queue[str]' = queue.Queue()
        expect = 0
        ans = []
        if cnt[0] < cnt[1] or cnt[0] == cnt[1] and s[0].isdigit():
            expect = 1
        for c in s:
            if c.isdigit():
                digit_queue.put(c)
            else:
                alpha_queue.put(c)
        while not(alpha_queue.empty() and digit_queue.empty()):
            if expect:
                ans.append(digit_queue.get())
            else:
                ans.append(alpha_queue.get())
            expect = 1 - expect
        return ''.join(ans)


s = Solution()

for i, (args, exp) in enumerate(zip(data['inputs'], data['outputs'])):
    assert_equal(s.reformat(*args), exp)
