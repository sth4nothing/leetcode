# -*- coding:utf-8 -*-
# 力扣解决方案
import bisect
import collections
import functools
import heapq
import itertools
import json
import queue
import re
from typing import (Any, Callable, Counter, DefaultDict, Dict, Iterable,
                    Iterator, List, Optional, Sequence, Set, Tuple, TypeVar)


def assert_equal(x: Any, eq: Any):
    if x == eq:
        print(f'⭕\t{x}=={eq}')
    else:
        print(f'❌\t{x}!={eq}')


data = json.loads('''
{"inputs":[[[["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]],[[["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]],[[["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]]],"outputs":[[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]],[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]],[["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]]}
''')


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        total: Dict[str, Counter[str]] = collections.defaultdict(collections.Counter)
        for name, table, food in orders:
            total[table][food] += 1
        tables = sorted(total.keys(), key=lambda x:int(x))
        foods = sorted(collections.ChainMap(*total.values()).keys())
        ans = [['Table'] + foods]
        for t in tables:
            line = [t]
            for f in foods:
                line.append(str(total[t][f]))
            ans.append(line)
        return ans


s = Solution()

for i, (args, exp) in enumerate(zip(data['inputs'], data['outputs'])):
    assert_equal(s.displayTable(*args), exp)
