class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1:
            return 1
        import heapq
        ugly = [1] * n
        heap = []
        for p in primes:
            heapq.heappush(heap, (p, p, 0))
        for i in range(1, n):
            while True:
                num, p, idx = heapq.heappop(heap)
                if num > ugly[i - 1]:
                    ugly[i] = num
                    heapq.heappush(heap, (ugly[idx + 1] * p, p, idx + 1))
                    break
                heapq.heappush(heap, (ugly[idx + 1] * p, p, idx + 1))
        return ugly[n - 1]
