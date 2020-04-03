from bisect import bisect_left


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __iter__(self):
        yield self
        if self.next:
            yield from self.next

    def __repr__(self):
        return ', '.join(str(n.val) for n in self)

    @staticmethod
    def parse(arr: 'List[int]') -> 'ListNode':
        dummy = ListNode(0)
        node = dummy
        for v in arr:
            node.next = ListNode(v)
            node = node.next
        head = dummy.next
        del dummy
        return head


class Solution:
    def nextLargerNodes(self, head: 'ListNode') -> 'List[int]':
        arr = list()
        res = list()
        node = ListNode(0)
        node.next = head
        idx = -1
        while node.next is not None:
            node = node.next
            idx += 1
            i = bisect_left(arr, (node.val, 0))
            if i > 0:
                for j in range(i):
                    res[arr[j][1]] = node.val
                arr[i - 1] = (node.val, idx)
                if i > 1:
                    arr = arr[i - 1:]
            else:
                arr.insert(0, (node.val, idx))
            res.append(0)
        return res


def main():
    s = Solution()
    print(s.nextLargerNodes(ListNode.parse([3, 3])))


if __name__ == "__main__":
    main()
