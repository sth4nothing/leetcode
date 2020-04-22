import collections
import functools
import heapq
import itertools
import queue
import re
from heapq import heapify, heappop, heappush
from typing import Any, Callable, Counter, Dict, Iterator, List, Set


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        words.sort(key=lambda x:len(x))
        ans = list()
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans

s = Solution()

inputs = [
    (["mass","as","hero","superhero"], ),
    (["leetcode","et","code"], ),
    (["blue","green","bu"], ),
    # ([[1,100000]],),
    # ([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],),
]
outputs = [
    ["as","hero"],
    ["et","code"],
    [],
    # 1,
    # 7,
]

for i, (args, exp) in enumerate(zip(inputs, outputs)):
    assertEqual(s.stringMatching(*args), exp)
