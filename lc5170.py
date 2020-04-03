import collections
from typing import Callable, List, Set, Any, Dict, Counter, Iterator

def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')

from queue import Queue
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        q: Queue[int] = Queue()
        visit: Set[int] = set()
        q.put(0)
        while not q.empty():
            k = q.get()
            if leftChild[k] != -1:
                if leftChild[k] in visit:
                    return False
                visit.add(leftChild[k])
                q.put(leftChild[k])
            if rightChild[k] != -1:
                if rightChild[k] in visit:
                    return False
                visit.add(rightChild[k])
                q.put(rightChild[k])
        return len(visit) == n - 1
        
s = Solution()

inputs = [
    (4, [1, -1, 3, -1], [2, -1, -1, -1],),
    (4, [1, -1, 3, -1], [2, 3, -1, -1],),
    (2, [1, 0], [-1, -1],),
    (6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1],),
    (3, [-1, 2, 1], [-1, -1, -1,])
    # ([[1,100000]],),
    # ([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],),
]
outputs= [
    True,
    False,
    False,
    False,
    False
    # 1,
    # 7,
]

for (args, exp) in zip(inputs, outputs):
    assertEqual(
        s.validateBinaryTreeNodes(*args),
        exp
    )

