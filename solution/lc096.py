class Solution:
    def __init__(self):
        self.trees = [1, 1]
    def numTrees(self, n: int) -> int:
        m = len(self.trees)
        if n < m:
            return self.trees[n]
        self.trees += [0] * (n + 1 - m)
        for i in range(m, n + 1):
            t = 0
            for v in range(m):
                t += self.trees[v] * self.trees[m - 1 - v]
            self.trees[i] = t
        return self.trees[n]

def main():
    s = Solution()
    print(s.numTrees(4))

main()
