class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        import collections
        d = collections.defaultdict(set)
        for u, v in edges:
            d[u].add(v)
            d[v].add(u)
        while len(d) > 2:
            vertexs = list(k for k in d if len(d[k]) == 1)
            for u in vertexs:
                v = d.pop(u)
                d[v.pop()].remove(u)
        return list(d.keys())
