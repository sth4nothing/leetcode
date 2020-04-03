import collections
import math
from typing import Callable, List, Set, Any, Dict, Counter, Iterator


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')

from queue import Queue
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a = math.floor(math.sqrt(num + 1))
        b = math.floor(math.sqrt(num + 2))
        for i in range(min(a, b)):
            c, r = divmod(num + 1, a - i)
            d, s = divmod(num + 2, b - i)
            if not r and not s:
                if c - a <= d - b:
                    return [a - i, c]
                else:
                    return [b - i, d]
            elif not r:
                return [a - i, c]
            elif not s:
                return [b - i, d]
        return [1, min(a, b)]
    def closestDivisors_2(self, num: int) -> List[int]:
        a = math.floor(math.sqrt(num + 1))
        b = math.floor(math.sqrt(num + 2))
        for i in range(a):
            c, r = divmod(num + 1, a - i)
            if r == 0:
                d = a - i
                break
        for i in range(b):
            e, r = divmod(num + 2, b - i)
            if r == 0:
                f = b - i
                break
        if c - d <= e - f:
            return [d, c]
        return [f, e]
        

s = Solution()

inputs = [
    (8,),
    (123,),
    (999,),
    (2,)
    # ([[1,100000]],),
    # ([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],),
]
outputs= [
    [3, 3],
    [5, 25],
    [25, 40],
    [2, 2]
    # 1,
    # 7,
]

for (args, exp) in zip(inputs, outputs):
    assertEqual(
        s.closestDivisors(*args),
        exp
    )

# from concurrent.futures import ThreadPoolExecutor
# def compare(num):
#     v1, v2 = s.closestDivisors(num), s.closestDivisors_2(num) 
#     if v1 != v2:
#         print(f'{v1}!={v2}')
#     elif num % 10000 == 0:
#         print(num)

# with ThreadPoolExecutor(16) as pool:
#     pool.map(compare, range(1, 10 ** 7))
