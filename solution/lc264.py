arr = [1]
pos = [0, 0, 0]
nums = (2, 3, 5)


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n > len(arr):
            for i in range(len(arr), n):
                arr.append(min(map(lambda x: arr[x[0]] * x[1], zip(pos, nums))))
                if arr[i] == arr[pos[0]] * 2:
                    pos[0] += 1
                if arr[i] == arr[pos[1]] * 3:
                    pos[1] += 1
                if arr[i] == arr[pos[2]] * 5:
                    pos[2] += 1
        return arr[n - 1]


s = Solution()
print(s.nthUglyNumber(10))
