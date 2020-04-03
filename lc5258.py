class Solution:
    def maxScoreWords(self, words: 'List[str]', letters: 'List[str]', score: 'List[int]') -> int:
        from collections import Counter
        words = [[w, 0] for w in words]
        letters = Counter(letters)
        for i in range(len(words)):
            word = Counter(words[i][0])
            words[i][1] = sum(score[ord(k) - ord('a')] * word[k] for k in word)
        def recurse(k, cnt: Counter):
            if k == len(words):
                return 0
            cnt.update(words[k][0])
            v1 = words[k][1] + recurse(k + 1, cnt) if not any(cnt[k] > letters[k] for k in cnt) else 0                
            cnt.subtract(words[k][0])
            v2 = recurse(k + 1, cnt)
            return max(v1, v2)
        return recurse(0, Counter())
s = Solution()
print(s.maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))