import collections
from typing import Callable, List, Set, Any, Dict, Counter, Iterator


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


from heapq import heapify, heappop, heappush
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        nums = [-v for v in target]
        heapify(nums)
        total, n = sum(nums), len(nums)
        while nums[0] != -1:
            m = heappop(nums)
            if m > -n:
                return False
            r = 2 * m - total
            total = m
            heappush(nums, r)
            if r != -1 and r > -n:
                return False
        return True


s = Solution()

inputs = [
    ([9,3,5],),
    ([1,1,11,9],),
    ([8,5],),
    # ([[1,100000]],),
    # ([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],),
]
outputs= [
    True,
    False,
    True,
    # 1,
    # 7,
]

for i, (args, exp) in enumerate(zip(inputs, outputs)):
    assertEqual(
        s.isPossible(*args),
        exp
    )

