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
{"inputs":[[1,3],[1,4],[3,9],[2,7],[10,100]],"outputs":["c","","cab","","abacbabacb"]}
''')


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        k -= 1
        chars = 'abc'
        ans: List[int] = []
        for i in reversed(range(n)):
            m, k = divmod(k, 2 ** i)
            if ans and (ans[-1] == 0 or ans[-1] == 1 and m > 0):
                m += 1
            if m > 2:
                return ''
            ans.append(m)
        return ''.join(map(lambda x: chars[x], ans))

s = Solution()
for args, eq in zip(data['inputs'], data['outputs']):
    assert_equal(s.getHappyString(*args), eq)
