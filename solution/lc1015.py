class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0:
            return -1
        nums = set()
        r = 0
        for i in range(1, K + 1):
            r = (r * 10 + 1) % K
            if r == 0:
                return i
            if r not in nums:
                nums.add(r)
            else:
                return -1
        return -1

def main():
    s = Solution()
    for i in range(1, 10**5 + 1):
        s.smallestRepunitDivByK(i)


if __name__ == "__main__":
    main()
