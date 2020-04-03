class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import operator
        ops = {'+': operator.add, '-': operator.sub}
        k, n = 0, len(s)
        res, op = None, None
        stack = []
        while k < n:
            if '0' <= s[k] <= '9':
                i = k + 1
                while i < n and '0' <= s[i] <= '9':
                    i += 1
                if res is None:
                    res = int(s[k:i])
                else:
                    res = ops[op](res, int(s[k:i]))
                k = i
            else:
                if s[k] == '(':
                    stack.append(op != '-')
                elif s[k] == ')':
                    stack.pop()
                elif s[k] in ops:
                    if not stack or stack[-1]:
                        op = s[k]
                    else:
                        op = '-' if s[k] == '+' else '+'
                k += 1
        return res
