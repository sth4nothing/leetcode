class Solution:
    def freqAlphabets(self, s: str) -> str:
        def str2chr(s: str) -> str:
            if len(s) == 1:
                return chr(ord('a') + int(s) - 1)
            return chr(ord('a') + int(s[:-1]) - 1)
        res = []
        j = None
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '#':
                j = i + 1
            elif j is None:
                res.append(str2chr(s[i]))
            elif j - i == 3:
                res.append(str2chr(s[i:j]))
                j = None
        return ''.join(res[::-1])


def assertEqual(x, eq):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')

s = Solution()

assertEqual(s.freqAlphabets('10#11#12'),
    'jkab')

assertEqual(s.freqAlphabets('1326#'),
    'acz')

assertEqual(s.freqAlphabets('25#'),
    'y')

assertEqual(s.freqAlphabets('25#'),
    'y')

assertEqual(s.freqAlphabets('12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#'),
    'abcdefghijklmnopqrstuvwxyz')

