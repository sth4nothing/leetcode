import collections
from typing import Any, Callable, Counter, Dict, List, Set, Tuple


def assertEqual(x: Any, eq: Any) -> None:
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


def alpha2pos(alpha: str) -> Tuple[int, int]:
    d = ord(alpha) - ord('A')
    return divmod(d, 6)

def dist(a1: str, a2: str) -> int:
    x1, y1 = alpha2pos(a1)
    x2, y2 = alpha2pos(a2)
    return abs(x1 - x2) + abs(y1 - y2)


class Solution:
    def minimumDistance(self, word: str) -> int:
        pass



s = Solution()
assertEqual(
    s.minimumDistance('CAKE'),
    3,
)

assertEqual(
    s.minimumDistance('HAPPY'),
    6,
)

assertEqual(
    s.minimumDistance('NEW'),
    3,
)

assertEqual(
    s.minimumDistance('YEAR'),
    7,
)
