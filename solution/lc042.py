class Solution:
    def next_extreme(self, s, low):
        while s < self.n - 1:
            if (low and self.nums[s] < self.nums[s + 1]) or (not low and self.nums[s] > self.nums[s + 1]):
                break
            else:
                s += 1
        return s

    def travel(self):
        if self.start >= self.n - 1:
            return
        self.mid = self.next_extreme(self.start + 1, True)
        if self.mid >= self.n - 1:
            return
        self.end = self.next_extreme(self.mid + 1, False)
        print(self.start, self.mid, self.end)
        h = min(self.nums[self.start], self.nums[self.end])
        for i in range(self.start, self.end + 1):
            self.arr[i] = h - self.nums[i] if h > self.nums[i] else 0
        self.start = self.end
        self.travel()

    def trap(self, height: 'List[int]') -> 'int':
        self.nums = height
        self.n = len(height)
        self.arr = [0] * self.n
        self.start = self.next_extreme(0, False)
        print(self.start)
        self.travel()
        return sum(self.arr)


Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
