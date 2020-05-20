#!/usr/bin/env python

# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode[{self.val}]"


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def helper(root: TreeNode, k: int, c: int) -> int:
            if root is None:
                return None, c

            val, c = helper(root.left, k, c)
            if val is not None:
                return val, c

            c += 1
            if c == k:
                return root.val, c

            return helper(root.right, k, c)

        val, _c = helper(root, k, 0)
        return val


s = Solution()

# Example 1
tree = TreeNode(3)
tree.right = TreeNode(4)
tree.left = TreeNode(1)
tree.left.right = TreeNode(2)
got = s.kthSmallest(tree, 1)
want = 1
print(f"got {got} want {want} pass? {got == want}")

# Example 2
tree = TreeNode(5)
tree.right = TreeNode(6)
tree.left = TreeNode(3)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.left.left.left = TreeNode(1)

for i in range(1, 6):
    got = s.kthSmallest(tree, i)
    want = i
    print(f"got {got} want {want} pass? {got == want}")
