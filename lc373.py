class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        heap = []
        n1, n2 = len(nums1), len(nums2)
        used = set()
        import heapq
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        while k > 0:
            i, j = heapq.heappop(heap)[1:]
            res.append((nums1[i], nums2[j]))
            if i < n1 - 1 and (i + 1, j) not in used:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                used.add((i + 1, j))
            if j < n2 - 1 and (i, j + 1) not in used:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                used.add((i, j + 1))
            k -= 1
            if i == n1 - 1 and j == n2 - 1:
                break
        return res
