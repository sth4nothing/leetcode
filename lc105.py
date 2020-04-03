# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '{}:[{},{}]'.format(self.val, self.left, self.right)


class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
        if len(preorder) == 0:
            return None
        preo = {v: k for k, v in enumerate(preorder)}
        inor = {v: k for k, v in enumerate(inorder)}

        def build(s, e):
            if e - s == 0:
                return None
            n = TreeNode(preorder[s])
            if e - s > 1:
                mid = inor[preorder[s]]
                idx = inor[preorder[s + 1]]
                if idx < mid:
                    if idx + 1 != mid:
                        n.left = build(s + 1, preo[inorder[mid - 1]] + 1)
                        n.right = build(preo[inorder[mid - 1]] + 1, e)
                    else:
                        n.left = build(s + 1, e)
                else:
                    n.right = build(s + 1, e)
            return n
        return build(0, len(preorder))


def main():
    s = Solution()
    print(s.buildTree([1, 2, 3],
                      [3, 2, 1]))


if __name__ == "__main__":
    main()
