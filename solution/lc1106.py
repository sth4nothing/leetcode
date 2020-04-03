import re


def A(*args):
    for v in args:
        if not v:
            return False
    return True


def O(*args):
    for v in args:
        if v:
            return True
    return False


def N(arg):
    return not arg


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def replace(c: re.Match):
            c = c.group()
            if c == '|':
                return 'O'
            if c == '!':
                return 'N'
            if c == '&':
                return 'A'
            if c == 't':
                return '1'
            if c == 'f':
                return '0'
            return c
        exp = re.sub(r'[|&!]', replace, expression)
        return eval(exp)


def main():
    s = Solution()
    print(s.parseBoolExpr("&(|(t,f,t),!(f))"))


if __name__ == "__main__":
    main()
