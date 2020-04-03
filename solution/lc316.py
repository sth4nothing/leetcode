class Node(object):
    def __init__(self, val=None, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt

    def __iter__(self):
        p = self if self.val is not None else self.nxt  # check if the node is dummy
        while p is not None:
            yield p.val
            p = p.nxt

    def __repr__(self):
        if self.val is not None:
            return '{}->{}'.format(self.val, self.nxt)
        else:
            return '[]->{}'.format(self.nxt)  # dummy head


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0] * 26
        head = Node()
        tail = head
        used = [False] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for c in s:
            ci = ord(c) - ord('a')
            cnt[ci] -= 1
            if used[ci]:
                continue
            p = tail
            while p is not head:
                cj = ord(p.val) - ord('a')
                if cj > ci and cnt[cj] > 0:
                    used[cj] = False
                    p.pre.nxt = p.nxt
                    if p is tail:
                        tail = tail.pre
                    else:
                        p.nxt.pre = p.pre
                    p = p.pre
                else:
                    break
            tail.nxt = Node(c, tail)
            tail = tail.nxt
            used[ci] = True
        return ''.join(head)
