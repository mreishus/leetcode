#!/usr/bin/env node

// Dynamic Programming approach - large memory usage
// 660ms, 104mb on leetcode
// I think this approach does too many comparisons 
// vs. a "expand only from current palindromes" 
// approach.
const countSubstrings = s => {
    let seen_pal = {};
    let pal_count = 0;

    for (let size = 1; size <= s.length; size++) {
        for (let start = 0; start + size - 1 < s.length; start++) {
            let end = start + size - 1;

            let is_pal = false;
            if (size == 1) {
                is_pal = true;
            } else if (size == 2) {
                is_pal = s[start] == s[end];
            } else {
                is_pal = (seen_pal[(start+1) + "-" + (end-1)]) && s[start] == s[end];
            }
            if (is_pal) {
                seen_pal[start + "-" + end] = true;
                pal_count += 1;
            }
        }
    }
    return pal_count;
};

let actualResult = countSubstrings("aaa");
let expectedResult = 6;
console.log("Expected result:", expectedResult);
console.log("Actual result:", actualResult);
let match = JSON.stringify(actualResult) == JSON.stringify(expectedResult);
console.log("Pass?", match);
