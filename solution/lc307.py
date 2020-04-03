class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.size = len(nums)
        self.arr = [0] * (self.size + 1)
        for i in range(1, self.size + 1):
            r = self._lowbit(i)
            for j in range(r):
                self.arr[i] += nums[i - j - 1]

    def _lowbit(self, x):
        return x & -x

    def _sum(self, i):
        res = 0
        while i > 0:
            res += self.arr[i]
            i -= self._lowbit(i)
        return res

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sum(j + 1) - self._sum(i)

    def _update(self, i, diff):
        while i <= self.size:
            self.arr[i] += diff
            i += self._lowbit(i)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.sumRange(i, i)
        self._update(i + 1, diff)


def main():
    nar = NumArray([1, 3, 5])
    print(nar.sumRange(0, 2))
    nar.update(1, 2)
    print(nar.sumRange(0, 2))


if __name__ == '__main__':
    main()
