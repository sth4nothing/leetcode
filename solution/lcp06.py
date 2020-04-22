import math
from typing import List
class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum(map(lambda c:math.ceil(c/2), coins))
