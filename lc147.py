from node import LinkedNode as ListNode


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(None)
        dummy.next = head
        while p.next:
            q = dummy
            while q is not p:
                if q.next.val > p.next.val:
                    t = p.next
                    p.next = p.next.next
                    t.next = q.next
                    q.next = t
                    break
                q = q.next
            else:
                p = p.next
        return dummy.next

class Solution2(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur = dummy
        while head:
            # check if it is needed to reset the cur pointer
            if cur and cur.val > head.val:
                cur = dummy
            # find the place to insert
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            # insert and sort the next element
            cur.next, cur.next.next, head = head, cur.next, head.next
        return dummy.next
