class Solution:
    def canThreePartsEqualSum(self, A: 'List[int]') -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        s //= 3
        t = 0
        a = []
        for i, v in enumerate(A):
            t += v
            if t == s:
                a.append(True)
                t = 0
                if len(a) == 2 and i + 1 < len(A):
                    return True
        return False

def main():
    s = Solution()
    print(s.canThreePartsEqualSum([0]))

if __name__ == "__main__":
    main()
