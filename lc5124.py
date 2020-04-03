from typing import List
import math
def count_digit(x):
    return int(math.log10(x))
def gen_num(s, c):
    return sum(i * 10 ** (c + s - i) for i in range(s, c + s + 1)) if c + s < 10 else 0
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lc = count_digit(low)
        c = 0
        s = low // 10 ** lc
        if lc + (low // 10 ** lc) > 9:
            s = 1
            c = lc + 1
        elif low <= sum(i * 10 ** (lc - i + s) for i in range(s, s + lc + 1)):
            c = lc
        elif s + lc < 9:
            s += 1
            c = lc
        else:
            s = 1
            c = lc + 1
        res = list()
        while True:
            v = gen_num(s, c)
            if v == 0 or v > high:
                break
            res.append(v)
            if s + c < 9:
                s += 1
            else:
                s = 1
                c += 1
        return res

print(Solution().sequentialDigits(10, 10**9))
