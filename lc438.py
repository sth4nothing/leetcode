from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> 'List[int]':
        if not s:
            return []
        chars = Counter(p) # aaa
        cnt = Counter()
        i, j, m, n = 0, 0, len(p), len(s)
        res = []
        while j < n:
            if s[j] not in chars:
                i = j = j + 1
                cnt.clear()
                continue
            cnt[s[j]] += 1
            j += 1
            if j - i == m:
                if chars == cnt:
                    res.append(i)
                cnt[s[i]] -= 1
                i += 1
        return res


# s = Solution()
# print(s.findAnagrams("cbaebabacd",
#                      "abc"))
