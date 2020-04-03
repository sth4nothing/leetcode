import collections

def abs(x: int) -> int:
    return x if x >= 0 else -x
class Solution:
    def balancedString(self, s: str) -> int:
        cnt = collections.Counter(s)
        cnt.update('QWER')
        n = len(s) // 4 + 1
        return sum(abs(v - n) for v in cnt.values()) // 2


s = Solution()
print(s.balancedString("WWEQERQWQWWRWWERQWEQ"))
