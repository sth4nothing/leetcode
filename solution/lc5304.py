from typing import List
def assertEqual(x, eq):
    print(f'{x}{("==" if x == eq else "!=")}{eq}')

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len (arr)
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        res: List[int] = list()
        for x, y in queries:
            res.append(prefix_xor[y + 1] ^ prefix_xor[x])
        return res

s = Solution()

assertEqual(s.xorQueries(
    [1,3,4,8],
    [[0,1],[1,2],[0,3],[3,3]]),
    [2,7,14,8])

assertEqual(s.xorQueries(
    [4,8,2,10],
    [[2,3],[1,3],[0,0],[0,3]]),
    [8,0,4,4])

