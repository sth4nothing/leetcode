class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        slow, fast, p = head, head, None
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        if p:
            p.next = None
        else:
            head = None
        tree = TreeNode(slow.val)
        tree.left = self.sortedListToBST(head)
        tree.right = self.sortedListToBST(slow.next)
        return tree
