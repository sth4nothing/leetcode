import itertools


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num < 1:
            return ['0:00']
        arr = [1, 2, 4, 8, 16, 32, 100, 200, 400, 800]
        times = [divmod(sum(arr[v] for v in x), 100)
                 for x in itertools.combinations(range(10), num)]
        times.sort()
        res = []
        for hour, minute in times:
            if hour < 13 and minute < 60:
                res.append('%d:%02d' % (hour, minute))
        return res
