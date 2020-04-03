class Solution:
    def longestSubsequence(self, arr: 'List[int]', difference: int) -> int:
        d = dict()
        n = len(arr)
        idxs = [1] * n
        for k, v in enumerate(arr):
            if v - difference not in d:
                if v not in d:
                    idxs[k] = 1
                    d[v] = k
                continue
            else:
                idxs[k] = idxs[d[v - difference]] + 1
                if v not in d or idxs[d[v]] < idxs[k]:
                    d[v] = k
        return max(idxs)


def main():
    s = Solution()
    print(s.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))


if __name__ == "__main__":
    main()
