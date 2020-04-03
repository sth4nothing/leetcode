class Solution:
    def minCostToMoveChips(self, chips: 'List[int]') -> int:
        cnt = [0, 0]
        for v in chips:
            cnt[v % 2] += 1
        return min(cnt)


def main():
    s = Solution()
    print(s.minCostToMoveChips([11]))


if __name__ == "__main__":
    main()
