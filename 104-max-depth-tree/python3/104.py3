#!/usr/bin/python3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1 + max( self.maxDepth(root.left), self.maxDepth(root.right) ) 

t1 = TreeNode(5)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)
expected_result = 3
s = Solution()
actual_result = s.maxDepth(t1)
print("Expect to see")
print(expected_result)
print("Actual Result")
print(actual_result)
print("Are same?")
print(actual_result == expected_result)

