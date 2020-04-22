import collections
import functools
import heapq
import itertools
import queue
import re
from heapq import heapify, heappop, heappush
from typing import Any, Callable, Counter, Dict, Iterator, List, Set


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


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
        return re.sub(r'&([^;]+);', repl, text)


s = Solution()

inputs = [
    ("&amp; is an HTML entity but &ambassador; is not.", ),
    ("and I quote: &quot;...&quot;", ),
    ("Stay home! Practice on Leetcode :)", ),
    ("x &gt; y &amp;&amp; x &lt; y is always false",),
    ("leetcode.com&frasl;problemset&frasl;all",),
]
outputs = [
    "& is an HTML entity but &ambassador; is not.",
    "and I quote: \"...\"",
    "Stay home! Practice on Leetcode :)",
    "x > y && x < y is always false",
    "leetcode.com/problemset/all",
]

for i, (args, exp) in enumerate(zip(inputs, outputs)):
    assertEqual(s.entityParser(*args), exp)
