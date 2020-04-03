from node import LinkedNode as ListNode


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p = d1 = ListNode(None)
        q = d2 = ListNode(None)
        d2.next = head
        while q.next:
            if q.next.val < x:
                p.next = q.next
                p = p.next
                q.next = q.next.next
                p.next = None
            else:
                q = q.next
        p.next = d2.next
        return d1.next
