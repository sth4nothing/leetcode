"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x * y
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> 'List[List[int]]':
        res = list()
        for x in range(1, 1001):
            if customfunction.f(x, 1) > z:
                break
            l, r = 1, 1001
            while l < r:
                y = (l + r) // 2
                z_ = customfunction.f(x, y)
                if z_ == z:
                    res.append((x, y))
                    break
                if y == l or y == r:
                    break
                if z_ > z:
                    r = y
                else:
                    l = y
        return res

s = Solution()
print(s.findSolution(CustomFunction(), 2809))
