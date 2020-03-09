#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0

        def pathSumChain(root: TreeNode, sum: int) -> int:
            if root is None:
                return 0
            answer = 0
            if root.val == sum:
                answer += 1
            answer += pathSumChain(root.left, sum - root.val)
            answer += pathSumChain(root.right, sum - root.val)
            return answer

        return (
            pathSumChain(root, sum)
            + self.pathSum(root.left, sum)
            + self.pathSum(root.right, sum)
        )
