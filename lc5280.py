# encoding=utf-8
import math
import functools
from typing import List, Dict, Any, Tuple, Callable
class Test:
    def __init__(self):
        self.cases: List[Tuple[Callable, Tuple[Any], Dict[str, Any], Any]] = list()
    def equal(self, expect, *args, **kwargs):
        def wrapper(func):
            self.cases.append((func, args, kwargs, expect))
            @functools.wraps(func)
            def inner_wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return inner_wrapper
        return wrapper
def div_ceil(x, y):
    return math.ceil(x / y)

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n, s = len(nums), sum(nums)
        if threshold == n:
            return max(nums)
        if threshold >= s:
            return 1
        def compare(x):
            return sum(div_ceil(v, x) for v in nums) - threshold
        l, r = div_ceil(s, threshold), div_ceil(s, threshold - n)
        ld, rd = compare(l), compare(r)
        while True:
            if r - l <= 1:
                return r if ld > 0 and rd <= 0 else l
            m = (l + r) // 2
            md = compare(m)
            if md > 0:
                l = m
                ld = md
            else:
                r = m
                rd = md

s = Solution()
# print(s.smallestDivisor([1, 2, 5, 9], 6))
# print(s.smallestDivisor([2,3,5,7,11], 11))
# print(s.smallestDivisor([19], 5))
# print(s.smallestDivisor([1,2,3], 1000000))
# print(s.smallestDivisor([962551,933661,905225,923035,990560],10))
# print(s.)
test = Test()
@test.equal(495280, [962551,933661,905225,923035,990560],10)
@test.equal(1, [1,2,3], 1000000)
@test.equal(5, [1, 2, 5, 9], 6)
@test.equal(55, [4813,3988,81,2197,6783,1729,7138,9317,176,2831,2352,4804,9470,5171,5504,5079,5875,3388,5199,1229,1089,2459,4592,5251,8538,8204,3992,3628,6031,7472,226,4317,7288,3688,593,343,5115,8813,4737,9559,2216,4436,1919,2386,5946,9904,6007,5652,8997,5491], 4394)
def smallestDivisor(nums, thresh):
    return s.smallestDivisor(nums, thresh)

for func, args, kwargs, expect in test.cases:
    try:
        res = func(*args, **kwargs)
        if res == expect:
            print(f'SUCCESS: {func.__name__}({", ".join(map(str, args))}, {", ".join(str(k) + "=" + str(v) for k, v in kwargs.items())}) == {expect}')
        else:
            print(f'FAILED: {func.__name__}({", ".join(map(str, args))}, {", ".join(str(k) + "=" + str(v) for k, v in kwargs.items())}) != {expect}')
    except Exception as e:
        print(f'ERROR: {func.__name__}({", ".join(map(str, args))}, {", ".join(str(k) + "=" + str(v) for k, v in kwargs.items())}) ?? {expect}')
