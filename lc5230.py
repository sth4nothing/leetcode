class Solution:
    def checkStraightLine(self, coordinates: 'List[List[int]]') -> bool:
        coordinates = {(x, y) for x, y in coordinates}
        n = len(coordinates)
        if n < 3:
            return True
        it = iter(coordinates)
        x1, y1 = next(it)
        x2, y2 = next(it)
        if x1 != x2:
            k = (y2 - y1) / (x2 - x1)
            for x, y in it:
                if x == x1:
                    return False
                if (y - y1) / (x - x1) != k:
                    return False
        else:
            for x, y in it:
                if x != x1:
                    return False
        return True


s = Solution()
print(s.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
