import bisect


class Solution:
    def longestArithSeqLength(self, A: 'List[int]') -> int:
        A.sort()
        ignore = set()
        la = len(A)
        if la < 3:
            return la
        res = 2
        for i in range(la):
            for j in range(i + 1, la):
                d = A[j] - A[i]
                if A[j] + d > A[-1]:
                    break
                r = A[i] if d == 0 else A[i] % d
                if (d, r) not in ignore:
                    ignore.add((d, r))
                else:
                    continue
                v = A[j]
                l = 2
                idx = j
                while True:
                    v += d
                    idx = bisect.bisect_left(A, v, idx + 1)
                    if idx < 0 or idx >= la or A[idx] != v:
                        break
                    else:
                        l += 1
                        res = max(res, l)
        return res


def main():
    s = Solution()
    print(s.longestArithSeqLength([0, 8, 45, 88, 48, 68, 28, 55, 17, 24]))

main()
