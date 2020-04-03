from bisect import bisect_left as search


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        cnt = [list() for _ in range(n)]
        res = ''
        for i, c in enumerate(s):
            j = t.find(c)
            if j == -1:
                continue
            cnt[j].append(i)
            if all(cnt[k] for k in range(n)):
                print(cnt)
                start = min(cnt[k][-1] for k in range(n))
                for k in range(n):
                    cnt[k] = cnt[k][search(cnt[k], start):]
                print(cnt)
                if i + 1 - start < len(res):
                    res = s[start:i + 1]
        return res


class Solution1(object):
    def minWindow(self, s, t):
        from collections import defaultdict
        i = j = 0
        count = len(t)
        step = float("inf")
        res = ""
        dic = defaultdict(int)
        for e in t:
            dic[e] += 1
        while j < len(s):
            if dic[s[j]] > 0:
                count -= 1
            dic[s[j]] -= 1
            j += 1
            while count == 0:
                if step > j-i:
                    step = j-i
                    res = s[i:j]
                if dic[s[i]] == 0:
                    count += 1
                dic[s[i]] += 1
                i += 1
        return res


def main():
    s = Solution1()
    print(s.minWindow("ADOBECODEBANC", 'ABC'))


if __name__ == "__main__":
    main()
