import collections
from typing import Callable, List, Set, Any, Dict, Counter, Iterator


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


from heapq import heapify, heappop, heappush
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        m, n = len(votes), len(votes[0])
        if m == 1:
            return votes[0]
        rank: Dict[str, List[int]] = dict()
        for i in range(m):
            for j in range(n):
                if votes[i][j] not in rank:
                    rank[votes[i][j]] = [0] * n
                rank[votes[i][j]][j] += 1
        return ''.join(k for k, v in sorted(rank.items(), key=lambda x:(x[1],-ord(x[0])), reverse=True))


s = Solution()

inputs = [
    (["ABC","ACB","ABC","ACB","ACB"],),
    (["WXYZ","XYZW"],),
    (["ZMNAGUEDSJYLBOPHRQICWFXTVK"],),
    (["BCA","CAB","CBA","ABC","ACB","BAC"],),
    (["M","M","M","M"],),
]
outputs= [
    "ACB",
    "XWYZ",
    "ZMNAGUEDSJYLBOPHRQICWFXTVK",
    "ABC",
    "M",
]

for i, (args, exp) in enumerate(zip(inputs, outputs)):
    assertEqual(
        s.rankTeams(*args),
        exp
    )

