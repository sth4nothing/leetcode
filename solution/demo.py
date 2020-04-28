# -*- coding:utf-8 -*-
# 力扣解决方案
import bisect
import collections
import functools
import heapq
import itertools
import json
import math
import re
from typing import (Any, Callable, Counter, DefaultDict, Dict, Iterable,
                    Iterator, List, Optional, Sequence, Set, Tuple, TypeVar)

import my_timer


@my_timer.timer_wrap
def assert_equal(fn: Callable, args: Sequence[Any], exp: Any):
    x = fn(*args)
    if x == exp:
        print(f'⭕\t{x}=={exp}')
    else:
        print(f'❌\t{x}!={exp}')


data = json.loads('''
{"inputs":[],"outputs":[]}
''')


import queue
from typing import *
class Solution:
    def fn(self, s: str) -> str:
        pass


s = Solution()

for i, (args, exp) in enumerate(zip(data['inputs'], data['outputs'])):
    assert_equal(s.fn, args, exp)
