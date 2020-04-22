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
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if rating[i] < rating[j] < rating[k]:
                        ans += 1
                    elif rating[i] > rating[j] > rating[k]:
                        ans += 1
        return ans
