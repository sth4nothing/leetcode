# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x: int):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None

from queue import Queue
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = Queue()
        q.put(root)
        res = "["
        while True:
            if q.qsize():
                if len(res) != 1:
                    res += ','
                n: TreeNode = q.get()
                if n is None:
                    res += 'null'
                else:
                    res += str(n.val)
                    q.put(n.left)
                    q.put(n.right)
            else:
                res += ']'
                break
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        s = data.index('[') + 1
        e = data.index(']', s)
        nodes = list(map(lambda x: TreeNode(int(x)) if x != 'null' else None, data[s:e].split(',')))
        i, j, k = 0, 1, len(nodes)
        while i < k:
            n = nodes[i]
            if n is not None:
                n.left = nodes[j]
                n.right = nodes[j + 1]
                j += 2
            i += 1
        return nodes[0] if k else None

 
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.right.right = TreeNode(5)

c = Codec()
print(c.serialize(c.deserialize(c.serialize(r))))
