class Solution:
    def maximumSum(self, arr: 'List[int]') -> int:
        f = [[-10000 for i in range(2)] for j in range(len(arr)+1)]
        ans = -10000
        for i in range(1, len(arr)+1):
            f[i][0] = max(f[i-1][0]+arr[i-1], arr[i-1])
            f[i][1] = max(f[i-1][0], f[i-1][1]+arr[i-1])
            ans = max(ans, max(f[i][0], f[i][1]))
        return ans



s=Solution()
print(s.maximumSum([1, 2, -1, -2, -1, 3]))
