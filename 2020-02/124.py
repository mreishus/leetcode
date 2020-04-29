#!/usr/bin/env python
"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path must
contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = -999999999

        def helper(root):
            nonlocal max_sum
            if root is None:
                return -9999999
            left = helper(root.left)
            right = helper(root.right)
            me_root_sum = root.val + max([0, left]) + max([0, right])
            max_sum = max([max_sum, me_root_sum])
            me_path_sum = max(
                [(root.val + max([0, left])), (root.val + max([0, right])),]
            )
            return me_path_sum

        helper(root)
        return max_sum
