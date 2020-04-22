# -*- coding:utf-8 -*-
import bisect
import collections
import functools
import heapq
import itertools
import json
import queue
import re
from typing import (Any, Callable, Counter, DefaultDict, Dict, Iterator, List,
                    Sequence, Set, Tuple)


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        return max((k for k, v in cnt.items() if k == v), default=-1)
