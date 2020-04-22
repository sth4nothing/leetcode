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
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        words.sort(key=lambda x: len(x))
        ans = list()
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans
