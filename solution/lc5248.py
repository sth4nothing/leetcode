class Solution:
    def numberOfSubarrays(self, nums: 'List[int]', k: int) -> int:
        odds = []
        x = 0
        for i, num in enumerate(nums):
            if num % 2 == 1:
                odds.append(x)
                x = 0
            else:
                x += 1
        odds.append(x)
        res = 0
        for i in range(len(odds) - k):
            res += (odds[i] + 1) * (odds[i + k] + 1)
        return res

s = Solution()
print(s.numberOfSubarrays([1,1,2,1,1], 3))
