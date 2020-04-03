import bisect

class Solution:
    def numSmallerByFrequency(self, queries: 'List[str]', words: 'List[str]') -> 'List[int]':
        def f(word: str) -> int:
            return word.count(min(word))
        qs = [f(q) for q in queries]
        ws = sorted([f(w) for w in words])
        n = len(ws)
        return [n - bisect.bisect_right(ws, q) for q in qs]

print(Solution().numSmallerByFrequency(["bbb","cc"],["a","aa","aaa","aaaa"]))
