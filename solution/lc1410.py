import re


class Solution:
    def entityParser(self, text: str) -> str:
        def repl(m):
            s = m.groups()[0]
            if s == 'quot':
                return '"'
            if s == 'apos':
                return '\''
            if s == 'amp':
                return '&'
            if s == 'gt':
                return '>'
            if s == 'lt':
                return '<'
            if s == 'frasl':
                return '/'
            return m.group()

        return re.sub(r'&(\w+);', repl, text)
