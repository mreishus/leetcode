#!/usr/bin/env node

// 60ms, 35MB on Leetcode - much better than 647-dynamic.js
// runtime 94th percentile, memory 50th percentile
const expand_palin_count = (s, i, j) => {
    let count = 0;
    while (i >= 0 && j < s.length && s[i] == s[j]) {
        count += 1;
        i -= 1;
        j += 1;
    }
    return count;
};
const countSubstrings = s => {
    let count = 0;
    for (let i = 0; i < s.length; i++) {
        count += expand_palin_count(s, i, i);
        count += expand_palin_count(s, i, i+1);
    }
    return count;
};

let actualResult = countSubstrings("aaa");
let expectedResult = 6;
console.log("Expected result:", expectedResult);
console.log("Actual result:", actualResult);
let match = JSON.stringify(actualResult) == JSON.stringify(expectedResult);
console.log("Pass?", match);
