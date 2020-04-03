class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        q = dummy = RandomListNode(-1)
        h = dict()
        while p is not None:
            k = hash(p)
            if k not in h:
                h[k] = RandomListNode(p.label)
            q.next = h[k]
            if p.random is not None:
                r = hash(p.random)
                if r not in h:
                    h[r] = RandomListNode(p.random.label)
                q.next.random = h[r]
            p, q = p.next, q.next
        return dummy.next
