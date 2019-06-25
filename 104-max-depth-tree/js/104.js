#!/usr/bin/env node

const TreeNode = val => ({
    val:  val,
    left: null,
    right: null,
});

const maxDepth = root => {
    if (root == null) {
        return 0;
    }
    return 1 + Math.max( maxDepth(root.left), maxDepth(root.right) );
};

const t1 = TreeNode(3);
t1.left = TreeNode(9);
t1.right = TreeNode(20);
t1.right.left = TreeNode(15);
t1.right.right = TreeNode(7);

const expected_result = 3;
const actual_result = maxDepth(t1);
console.log("Expected result:", expected_result);
console.log("Actual result:", actual_result);
console.log("Equal?", expected_result == actual_result);
