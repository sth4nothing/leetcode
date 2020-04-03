import collections
from typing import Callable, List, Set, Any, Dict, Counter, Iterator


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(1 if val < 0 else 0 for row in grid for val in row)


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


s = Solution()

inputs = [
    ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],),
    ([[3, 2], [1, 0]],),
    ([[1, -1], [-1, -1]],),
    ([[-1]],),
]
outputs= [
    8,
    0,
    3,
    1,
]

for i in range(len(inputs)):
    assertEqual(
        s.countNegatives(*inputs[i]),
        outputs[i]
    )
