#!/usr/bin/env python
"""
Return the root node of a binary search tree that matches the given preorder
traversal.

(Recall that a binary search tree is a binary tree where for every node, any
descendant of node.left has a value < node.val, and any descendant of
node.right has a value > node.val.  Also recall that a preorder traversal
displays the value of the node first, then traverses node.left, then traverses
node.right.)

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

      8
  5       10
1   7         12
"""


from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def binsearch_larger(i, j, target):
            low = i
            high = j
            result = None
            while low <= high:
                mid = (low + high) // 2
                if preorder[mid] < target:
                    low = mid + 1
                elif preorder[mid] == target:
                    low = mid + 1
                else:  # preorder[mid] > target
                    if result is None or mid < result:
                        result = mid
                    high = mid - 1
            return result

        def helper(i, j) -> TreeNode:
            if j < i:
                return None

            head = TreeNode(preorder[i])
            if i == j:
                return head

            first_larger = binsearch_larger(i + 1, j, preorder[i])
            if first_larger is None:
                first_larger = j + 1

            # Linear Search
            # first_larger = j + 1
            # for x in range(i + 1, j + 1):
            #     if preorder[x] > preorder[i]:
            #         first_larger = x
            #         print(f"Found first larger, val {preorder[x]} indx {x}")
            #         break

            # print(f" left --> {i + 1} {first_larger - 1}")
            left = helper(i + 1, first_larger - 1)
            # print(f" right --> {first_larger} {j}")
            right = helper(first_larger, j)
            head.left = left
            head.right = right
            return head

        return helper(0, len(preorder) - 1)


if __name__ == "__main__":
    A = [7, 20, 19, 12]
    got = Solution().bstFromPreorder(A)
    print(got)
    # A = [4, 5, 14, 20]
    # got = Solution().bstFromPreorder(A)
    # print(got)
    # A = [8, 5, 1, 7, 10, 12]
    # got = Solution().bstFromPreorder(A)
    # print(got)
