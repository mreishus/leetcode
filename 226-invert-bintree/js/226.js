#!/usr/bin/env node

let invertTree = root => {
    if (root == null) {
        return null;
    }
    let tmp = root.right;
    root.right = invertTree(root.left);
    root.left = invertTree(tmp);
    return root;
};
