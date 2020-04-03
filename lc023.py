# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap = []
        for k in range(len(lists)):
            if lists[k]:
                heapq.heappush(heap, (lists[k].val, k))
        head = ListNode(None)
        p = head
        while heap:
            k = heapq.heappop(heap)[1]
            node = lists[k]
            lists[k] = node.next
            p.next, node.next = node, None
            p = p.next
            if lists[k]:
                heapq.heappush(heap, (lists[k].val, k))
        return head.next
