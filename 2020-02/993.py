#!/usr/bin/env python

"""
993. Cousins in Binary Tree
Easy

In a binary tree, the root node is at depth 0, and children of each depth k
node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have
different parents.

We are given the root of a binary tree with unique values, and the values x and
y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are
cousins.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = [root]
        while len(q) > 0:
            next_level = []

            this_level_vals = [n.val for n in q]
            if x in this_level_vals and y in this_level_vals:
                return True

            for node in q:
                children = []
                if node.left:
                    next_level.append(node.left)
                    children.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    children.append(node.right.val)
                if x in children and y in children:
                    return False

            q = next_level
        return False


if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.right = TreeNode(4)
    t.right.right = TreeNode(5)
    print("Expect: True")
    print(Solution().isCousins(t, 4, 5))
