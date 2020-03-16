#!/usr/bin/env python

from typing import Any, List
from functools import lru_cache

# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def numTreesSlow(self, n: int) -> int:
        @lru_cache(None)
        def findTrees(low, high) -> List[TreeNode]:
            if low > high:
                return [None]

            results = []
            for i in range(low, high + 1):
                left_trees = findTrees(low, i - 1)
                right_trees = findTrees(i + 1, high)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        top = TreeNode(i, left_tree, right_tree)
                        results.append(top)

            return results

        return len(findTrees(1, n))

    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def findTrees(low, high) -> int:
            if low > high:
                return 1

            results = 0
            for i in range(low, high + 1):
                left_trees = findTrees(low, i - 1)
                right_trees = findTrees(i + 1, high)
                results += left_trees * right_trees

            return results

        return findTrees(1, n)


if __name__ == "__main__":
    S = Solution()
    print("hi")
    print("expect to see: 5")
    print(S.numTrees(3))
    print("expect to see: ?? [Answer for 4]")
    print(S.numTrees(4))
    print("expect to see: ?? [Answer for 5]")
    print(S.numTrees(5))
    print("expect to see: ?? [Answer for 12]")
    print(S.numTrees(12))
