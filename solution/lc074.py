class Solution:
    def getVal(self, matrix: 'List[List[int]]', idx: int):
        return matrix[idx // self.w][idx % self.w]

    def search(self, matrix: 'List[List[int]]', target: int, low: int, high: int):
        if low > high:
            return -1
        if low == high:
            return low
        mid = (low + high) // 2
        val = self.getVal(matrix, mid)
        if target < val:
            return self.search(matrix, target, low, mid)
        if target > val:
            return self.search(matrix, target, mid + 1, high)
        return mid

    def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        # binary search
        self.h = len(matrix)
        if self.h <= 0:
            return False
        self.w = len(matrix[0])
        self.size = self.h * self.w
        idx = self.search(matrix, target, 0, self.size)
        if idx != -1 and 0 <= idx < self.size and self.getVal(matrix, idx) == target:
            return True
        return False

def main():
    s = Solution()
    print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 49))

main()
