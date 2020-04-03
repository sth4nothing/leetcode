class Solution:
    def maxScoreSightseeingPair(self, A: 'List[int]') -> int:
        arr1 = list(v + i for i, v in enumerate(A))
        arr2 = list(v - i for i, v in enumerate(A))
        i, j = 0, len(A) - 1
        mmax = 0
        while i < j:
            mmax = max(arr1[i] + arr2[j], mmax)
            if arr1[i + 1] - arr1[i] > arr2[j - 1] - arr2[j]:
                i += 1
            else:
                j -= 1
        return mmax

def main():
    s = Solution()
    print(s.maxScoreSightseeingPair([3, 7, 2, 3]))

if __name__ == "__main__":
    main()
