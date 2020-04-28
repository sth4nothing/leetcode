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

import my_timer

@my_timer.timer_wrap
def assert_equal(fn, args, exp: Any):
    x = fn(*args)
    if x == exp:
        print(f'⭕\t{x}=={exp}')
    else:
        print(f'❌\t{x}!={exp}')


data: Dict[str, List[Any]] = json.loads('''
{"inputs":[[[[1,2,3],[4,5,6],[7,8,9]]],[[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]],[[[1,2,3],[4],[5,6,7],[8],[9,10,11]]],[[[1,2,3,4,5,6]]]],"outputs":[[1,4,2,7,5,3,8,6,9],[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16],[1,4,2,5,3,8,6,9,7,10,11],[1,2,3,4,5,6]]}
''')


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        ans: List[List[int]] = []
        for i in range(n):
            for j in range(len(nums[i])):
                if i + j >= len(ans):
                    ans.append([])
                ans[i + j].append(nums[i][j])
        return [v for arr in ans for v in reversed(arr)]


s = Solution()
for args, eq in zip(data['inputs'], data['outputs']):
    assert_equal(s.findDiagonalOrder, args, eq)
