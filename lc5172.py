import collections
from typing import Callable, List, Set, Any, Dict, Counter, Iterator


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')

from queue import Queue
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        n = len(digits)
        one, two = sum(int(d % 3 == 1) for d in digits), sum(int(d % 3 == 2) for d in digits)
        one_3, two_3 = one % 3, two % 3
        if one_3 != two_3:

            if two_3 - one_3 == 1 or one_3 + two_3 == 2 and (one == 0 or two_3 == 0 and two > 0):
                c = 2 if one == 0 and two_3 == 2 else 1
                r = 2
            else:
                c = 2 if two == 0 and one_3 == 2 else 1
                r = 1
            
            for i in range(n - 1, -1, -1):
                if digits[i] % 3 == r:
                    c -= 1
                    digits.pop(i)
                    if c <= 0:
                        break
        
        if not digits:
            return ''
        if digits[0] == 0:
            return '0'
        return ''.join(map(str, digits))

        


s = Solution()

inputs = [
    ([8,1,9],),
    ([8,6,7,1,0],),
    ([1],),
    ([1,0,0,0,0,0],),
    # ([[1,100000]],),
    # ([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]],),
]
outputs= [
    '981',
    '8760',
    '',
    '0',
    # 1,
    # 7,
]

for (args, exp) in zip(inputs, outputs):
    assertEqual(
        s.largestMultipleOfThree(*args),
        exp
    )

