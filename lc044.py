class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        p = re.sub(r'\*+', '*', p)
        ns = len(s)
        np = len(p)
        hist = set()

        def match(idxs=0, idxp=0) -> bool:
            if (idxs, idxp) in hist:
                return False
            else:
                hist.add((idxs, idxp))
            if idxs >= ns and idxp >= np:
                return True
            elif idxp >= np:
                return False
            elif idxs >= ns:
                return idxp == np - 1 and p[idxp] == '*'
            if p[idxp] == '?':
                return match(idxs + 1, idxp + 1)
            if p[idxp] != '*':
                return s[idxs] == p[idxp] and match(idxs + 1, idxp + 1)
            qst = 0
            nxts, nxtp = idxs, idxp
            while nxtp < np:
                if p[nxtp] == '?':
                    qst += 1
                elif p[nxtp] != '*':
                    break
                nxtp += 1
            else:
                return ns - idxs >= qst
            nxtpe = nxtp + 1
            while nxtpe < np:
                if p[nxtpe] not in '?*':
                    nxtpe += 1
                else:
                    break
            while True:
                nxts = s.find(p[nxtp:nxtpe], nxts)
                if nxts == -1:
                    return False
                if nxts - idxs >= qst and match(nxts + nxtpe - nxtp, nxtpe):
                    return True
                nxts += 1
        return match(0, 0)


class Solution1:
    def isMatch(self, s: str, p: str) -> bool:        
        si = pi = 0
        ssi = spi = None  # '*' indexes
        sl, pl = len(s), len(p)
        while si < sl:
            if pi < pl and p[pi] == '*':
                ssi, spi = si, pi
                pi += 1
            elif pi < pl and (p[pi] == s[si] or p[pi] == '?'):
                si, pi = si+1, pi+1
            elif spi is not None:
                si, pi = ssi+1, spi+1
                ssi += 1
            else:
                return False

        while pi < pl and p[pi] == '*':
            pi += 1

        return pi == pl


ans = Solution().isMatch("adceb",
                         "*a*b")
print(ans)
