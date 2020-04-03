import ctypes


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b:
            a, b = ctypes.c_int32(a).value, ctypes.c_int32(b).value
            a, b = a ^ b, (a & b) << 1
        return a
