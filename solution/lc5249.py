class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        remove = list()
        lefts = list()
        for j in range(n):
            if s[j] == '(':
                lefts.append(j)
            elif s[j] == ')':
                if lefts:
                    lefts.pop(-1)
                else:
                    remove.append(j)
        remove.extend(lefts)
        if len(remove) == 0:
            return s
        strs = []
        i = 0
        for j in remove:
            strs.append(s[i:j])
            i = j + 1
        if i < n:
            strs.append(s[i:])
        return ''.join(strs)


s = Solution()
print(s.minRemoveToMakeValid('(a(b(c)d)'))
