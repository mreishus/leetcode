#!/usr/bin/node
const TreeNode = (val) => ({
    val: val,
    left: null,
    right: null,
});

let mergeTrees = function(t1, t2) {
    if (t1 == null) {
        return t2;
    }
    if (t2 == null) {
        return t1;
    }
    t1.val += t2.val;
    t1.left = mergeTrees(t1.left, t2.left);
    t1.right = mergeTrees(t1.right, t2.right);
    return t1;
};

let et1 = TreeNode(1);
et1.left = TreeNode(3);
et1.left.left = TreeNode(5);
et1.right = TreeNode(2);

let et2 = TreeNode(2);
et2.left = TreeNode(1);
et2.left.right = TreeNode(4);
et2.right = TreeNode(3);
et2.right.right = TreeNode(7);

let actualResult = mergeTrees(et1, et2);
console.log(actualResult);
