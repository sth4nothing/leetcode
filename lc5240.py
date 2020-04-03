import collections


class Solution:
    def maxLength(self, arr: 'List[str]') -> int:
        n = len(arr)
        if n == 0:
            return 0
        const = (1 << 27) - 1
        cnts = [collections.Counter(s) for s in arr]
        nums = [0] * n
        ok = [set() for _ in range(n)]
        for i, cnt in enumerate(cnts):
            for k in cnt:
                if cnt[k] > 1:
                    nums[i] = const
                    break
                nums[i] += 1 << ord(k) - ord('a')
        del cnts
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] & nums[j] == 0:
                    ok[i].add(j)
                    ok[j].add(i)
        ans = dict()
        visit = [0] * n

        def foo(p: int, s: int, interset: set):
            if visit[p] or p not in interset:
                return s
            s += len(arr[p])
            visit[p] = 1
            tp = tuple(visit)
            if tp not in ans:
                t = interset.intersection(ok[p])
                res = max((foo(q, s, t) for q in ok[p]), default=s)
                if sum(visit) != 0:
                    ans[tp] = res
            else:
                res = ans[tp]
            visit[p] = 0
            return res
        ss = set(i for i in range(n) if nums[i] != const)
        return max((foo(i, 0, ss) for i in range(n)), default=0)


s = Solution()
print(s.maxLength(["cha", "r", "act", "ers"]))
