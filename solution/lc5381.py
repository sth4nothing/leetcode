import collections
import functools
import heapq
import itertools
import queue
import re
import bisect
from heapq import heapify, heappop, heappush
from typing import Any, Callable, Counter, Dict, Iterator, List, Set


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        def find(array: List[int], x: int):
            i = bisect.bisect_left(array, x)
            exists = i < len(array) and x == array[i]
            return i, exists
        ans: List[int] = list()
        queried_list: List[int] = list()
        queried_set: List[int] = list()
        for x in queries:
            idx, exists = find(queried_set, x)
            if exists:
                q_idx = queried_list.index(x)
                ans.append(len(queried_list) - 1 - q_idx)
                for i in range(q_idx, len(queried_list) - 1):
                    queried_list[i] = queried_list[i + 1]
                queried_list[-1] = x
            else:
                ans.append(x - 1 + len(queried_set) - idx)
                queried_list.append(x)
                queried_set.insert(idx, x)
        return ans


s = Solution()

inputs = [
    ([3,1,2,1], 5,),
    ([4,1,2,2], 4,),
    ([7,5,5,8,3], 8,),
    # ([[1,100000]],),
    # ([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],),
]
outputs = [
    [2,1,2,1],
    [3,1,2,0],
    [6,5,0,7,5],
    # 1,
    # 7,
]

for i, (args, exp) in enumerate(zip(inputs, outputs)):
    assertEqual(s.processQueries(*args), exp)
