class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self):
        return '{ ' + str(self.val) +': ' + repr(self.left) + ', ' + repr(self.right) + '}'


class Solution:
    def getDepth(self, S: str):
        end = self.idx
        while end < self.len:
            if S[end] == '-':
                end += 1
            else:
                break
        res = end - self.idx
        self.idx = end
        return res

    def getVal(self, S: str):
        end = self.idx
        while end < self.len:
            if S[end] != '-':
                end += 1
            else:
                break
        res = 0 if end - self.idx < 1 else int(S[self.idx:end])
        self.idx = end
        return res

    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.len = len(S)
        self.idx = 0
        if self.len == 0:
            return None
        self.root = TreeNode(self.getVal(S))
        self.stack = [self.root]
        while self.idx < self.len:
            d = self.getDepth(S)
            v = self.getVal(S)
            n = TreeNode(v)
            while d < len(self.stack):
                self.stack.pop()
            if self.stack[-1].left is None:
                self.stack[-1].left = n
                self.stack.append(n)
            elif self.stack[-1].right is None:
                self.stack[-1].right = n
                self.stack.append(n)
        return self.root


def main():
    s = Solution()
    print(s.recoverFromPreorder("1-2--3--4-5--6--7"))

main()
