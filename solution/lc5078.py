class Solution:
    def addNegabinary(self, arr1: 'List[int]', arr2: 'List[int]') -> 'List[int]':
        n = max(len(arr1), len(arr2))
        res = []
        for i in range(-1, -n - 1, -1):
            r = 0
            if len(arr1) + i >= 0:
                r += arr1[i]
            if len(arr2) + i >= 0:
                r += arr2[i]
            res.append(r)
        i = 0
        while i < len(res):
            if res[i] == 0:
                i += 1
                continue
            n, r = divmod(res[i], 2)
            res[i] = r
            if n > 0:
                if i + 1 >= len(res):
                    res.append(0)
                if res[i + 1] >= n:
                    res[i + 1] -= n
                    n = 0
                else:
                    n -= res[i + 1]
                    res[i + 1] = n
                    if i + 2 >= len(res):
                        res.append(0)
                    res[i + 2] += n
            i += 1
        for j in range(len(res) - 1, -1, -1):
            if res[j] != 0:
                return res[j::-1]
        return [0]


def main():
    s = Solution()
    print(s.addNegabinary([1, 1, 0], [0, 1, 0]))


if __name__ == "__main__":
    main()
