import collections
from typing import Callable, List, Set, Any, Dict, Counter, Iterator


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


import datetime
first = datetime.datetime(1, 1, 1)
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def days(date: str) -> int:
            return (datetime.datetime.strptime(date, '%Y-%m-%d') - first).days
        return abs(days(date1) - days(date2))

s = Solution()

inputs = [
    ("2019-06-29", "2019-06-30",),
    ("2020-01-15", "2019-12-31",),
    # ([[1,100000]],),
    # ([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],),
]
outputs= [
    1,
    15,
    # 1,
    # 7,
]

for (args, exp) in zip(inputs, outputs):
    assertEqual(
        s.daysBetweenDates(*args),
        exp
    )

