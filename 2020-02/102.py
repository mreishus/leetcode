#!/usr/bin/env python

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [root]
        result = []
        if root is None:
            return result

        while len(q) > 0:
            this_level_vals = [node.val for node in q]
            result.append(this_level_vals)
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return result


if __name__ == "__main__":
    print("HI")
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)
    z = Solution().levelOrder(t)
    print(z)
