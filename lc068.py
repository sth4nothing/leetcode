class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        k, n = 0, len(words)
        res = []
        while k < n:
            l = len(words[k])
            i = 1
            while k + i < n and l + 1 + len(words[k + i]) <= maxWidth:
                l += 1 + len(words[k + i])
                i += 1
            sp = maxWidth - l + i - 1
            line = words[k]
            if i == 1:
                line += ' ' * sp
            elif k + i < n:
                for j in range(1, i):
                    line += ' ' * (sp // (i - 1) + (1 if j <= sp % (i - 1) else 0)) + words[k + j]
            else:
                for j in range(1, i):
                    line += ' ' + words[k + j]
                line += ' ' * (sp - i + 1)
            res.append(line)
            k += i
        return res
