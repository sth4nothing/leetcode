from typing import Callable, List, Set, Any, Dict, Counter
def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        arr = [bin(x)[2:] for x in (a, b, c)]
        max_len = max(len(x) for x in arr)
        a_, b_, c_ = ([v == '1' for v in x.rjust(max_len, '0')] for x in arr)
        res = 0
        for i in range(max_len):
            if (a_[i] or b_[i]) == c_[i]:
                continue
            if c_[i]:
                res += 1
            else:
                res += a_[i] + b_[i]
        return res

s = Solution()

assertEqual(
    s.minFlips(2, 6, 5),
    3)
assertEqual(
    s.minFlips(4, 2, 7),
    1)
assertEqual(
    s.minFlips(1, 2, 3),
    0)