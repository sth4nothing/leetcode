class Solution(object):
    def check(self, val, z):
        if z == val:
            return True
        if val not in self.set:
            self.set.add(val)
            self.valid.append(val)
        return False

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x < y:
            x, y = y, x
        if z == 0 or z == x or z == y or z == x + y or z == x - y:
            return True
        if z > x + y or z < 0:
            return False
        if x - y == 1 or y == 1:
            return True
        self.valid = [x, y, x - y]
        self.set = set()
        k = 2
        while True:
            n = len(self.valid)
            while k < n:
                if self.valid[k] < y:
                    if self.check(x - y + self.valid[k], z):
                        return True
                if self.valid[k] > y:
                    if self.check(self.valid[k] - y, z):
                        return True
                if self.valid[k] + y > x:
                    if self.check(y - x + self.valid[k], z):
                        return True
                k += 1
            if len(self.valid) == n:
                break
        k, n = 2, len(self.valid)
        while k < n:
            if self.valid[k] < y:
                if self.valid[k] + x == z:
                    return True
            if self.valid[k] + y == z:
                return True
        return False
