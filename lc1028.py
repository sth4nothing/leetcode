from collections import Counter
from math import log2
import heapq


class Solution:
    def idx(self, num: int):
        return int(log2(num if num >= 0 else -num) + 0.5)

    def recurse(self, num: int):
        k = self.idx(num)
        return num - (-2) ** k, k

    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        idxs = Counter()
        while N != 0:
            N, k = self.recurse(N)
            idxs[k] += 1
        keys = list(idxs.keys())
        heapq.heapify(keys)
        while len(keys) > 0:
            k = heapq.heappop(keys)
            if idxs[k] <= 1:
                continue
            n, r = divmod(k, 2)
            if (k + 1) not in idxs:
                heapq.heappush(keys, k + 1)
            if (k + 2) not in idxs:
                heapq.heappush(keys, k + 2)
            if r == 0:
                idxs.pop(k)
            else:
                idxs[k] = r
            idxs[k + 1] += n
            idxs[k + 2] += n
        mi = max(idxs)
        return ''.join(map((lambda x: '1' if x in idxs else '0'), range(mi, -1, -1)))

s = Solution()
s.baseNeg2(22)
