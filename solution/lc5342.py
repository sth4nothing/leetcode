import collections

from typing import Callable, List, Set, Any, Dict, Counter, Iterator

def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


from heapq import heapify, heappop, heappush
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        heap: List[int] = list()
        i, j, ans = 0, 0, 0
        while j < n or heap:
            while j < n and events[j][0] == i:
                heappush(heap, events[j][1])
                j += 1
            while heap and heap[0] < i:
                heappop(heap)
            if heap:
                heappop(heap)
                ans += 1
            i += 1
        return ans

s = Solution()

inputs = [
    ([[1,2],[2,3],[3,4]],),
    ([[1,2],[2,3],[3,4],[1,2]],),
    ([[1,4],[4,4],[2,2],[3,4],[1,1]],),
    ([[1,100000]],),
    ([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],),
]
outputs= [
    3,
    4,
    4,
    1,
    7,
]

for i in range(len(inputs)):
    assertEqual(
        s.maxEvents(*inputs[i]),
        outputs[i]
    )
