import collections
from typing import DefaultDict, Dict, List, Set, Tuple


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        d: DefaultDict[int, Set[int]] = collections.defaultdict(set)
        for x, y in relation:
            d[y].add(x)
        dp: Dict[Tuple[int, int], int] = dict()

        def pass_away(p, k):
            if k == 0:
                return 0 if p != 0 else 1
            if (p, k) not in dp:
                d[(p, k)] = sum(pass_away(v, k - 1) for v in d[p])
            return d[(p, k)]

        return pass_away(n - 1, k)
