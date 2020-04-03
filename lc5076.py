class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        m = len(str1)
        n = len(str2)
        if n == 0 or str1[0] != str2[0]:
            return ''
        def gcd(a, b):
            r = a % b
            if r == 0:
                return b
            return gcd(b, r)
        g = gcd(m, n)
        import re
        for i in range(g + 1, 0, -1):
            if g % i != 0:
                continue
            pat = f'({str1[:i]})+'
            if re.fullmatch(pat, str1) and re.fullmatch(pat, str2):
                return str1[:i]
        return ''

def main():
    s = Solution()
    print(s.gcdOfStrings('LEET', 'CODE'))


if __name__ == "__main__":
    main()
