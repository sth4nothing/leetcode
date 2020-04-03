class Solution:
    def dieSimulator(self, n: int, rollMax: 'List[int]') -> int:
        dp = [[0] * 6 for _ in range(n)]
        m = 10 ** 9 + 7
        for i in range(6):
            dp[0][i] = 1
        for j in range(1, n):
            s = sum(dp[j - 1]) % m
            for i in range(6):
                dp[j][i] = s
                if j > rollMax[i] > 1:
                    dp[j][i] -= sum(dp[j - rollMax[i] - 1]) - dp[j - rollMax[i] - 1][i]
                elif j >= rollMax[i]:
                    dp[j][i] -= dp[j - rollMax[i]][i]
        return sum(dp[n - 1]) % m


s = Solution()
print(s.dieSimulator(2, [1,1,2,2,2,3]))


# 4
# [2,1,1,3,3,2]
# 1082
# 4
# [2,3,1,1,1,2]
# 991
