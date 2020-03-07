#!/usr/bin/env python

# 543. Diameter of Binary Tree
# Easy

# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree

#           1
#          / \
#         2   3
#        / \
#       4   5

# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        l = self.diameterOfBinaryTree(root.left)
        r = self.diameterOfBinaryTree(root.right)
        h = self.height(root.left) + self.height(root.right)

        return max([r, l, h])

    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    s = Solution()
    print(s.diameterOfBinaryTree(root))
