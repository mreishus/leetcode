#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
        def invertTree(self, root: TreeNode) -> TreeNode:
            if (root == None):
                return None
            tmp = root.right
            root.right = self.invertTree(root.left)
            root.left = self.invertTree(tmp)
            return root

t1 = TreeNode(5)
s = Solution()
a = s.invertTree(t1)
print(a)
