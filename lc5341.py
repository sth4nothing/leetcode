import collections
from typing import Callable, List, Set, Any, Dict, Counter, Iterator


def assertEqual(x: Any, eq: Any):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')


# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         return sum(1 if val < 0 else 0 for row in grid for val in row)


# s = Solution()

# inputs = [
#     ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],),
#     ([[3, 2], [1, 0]],),
#     ([[1, -1], [-1, -1]],),
#     ([[-1]],),
# ]
# outputs= [
#     8,
#     0,
#     3,
#     1,
# ]

# for i in range(len(inputs)):
#     assertEqual(
#         s.countNegatives(*inputs[i]),
#         outputs[i]
#     )


class ProductOfNumbers:

    def __init__(self):
        self.products = [1]
        self.zero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.products.append(1)
            self.zero = len(self.products) - 1
        elif self.products[-1]:
            self.products.append(self.products[-1] * num)
        else:
            self.products.append(num)

    def getProduct(self, k: int) -> int:
        if len(self.products) - k > self.zero:
            return self.products[-1] // self.products[-k - 1]
        else:
            return 0


s = ProductOfNumbers()

inputs = [
    "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add", "getProduct"
]
args = [
    [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]
]
outputs = [
    None, None, None, None, None, 20, 40, 0, None, 32
]
for i, (func, arg, exp) in enumerate(zip(inputs, args, outputs)):
    assertEqual(
        s.__getattribute__(inputs[i])(*arg),
        exp
    )
