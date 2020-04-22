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
{"inputs":[[2,3,1],[5,2,3],[9,1,1],[50,100,25],[37,17,7]],"outputs":[6,0,1,34549172,418930126]}
''')


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        pass


s = Solution()

for i, (args, exp) in enumerate(zip(data['inputs'], data['outputs'])):
    assert_equal(s.numOfArrays(*args), exp)
