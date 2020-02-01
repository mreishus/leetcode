#!/usr/bin/env node

var hammingDistance = function(x, y) {
    // Use XOR
    let difference = x ^ y;
    console.log(difference);
    // Now, count the number of 1s in a binary representation of difference
    let count = 0;
    while (difference > 0) {
        if (difference % 2 == 1) {
            count++;
        }
        difference = difference >> 1;
    }
    return count;
};

let actualResult = hammingDistance(1, 4);
let expectedResult = 2;
console.log("Expected result:", expectedResult);
console.log("Actual result:", actualResult);
let match = JSON.stringify(actualResult) == JSON.stringify(expectedResult);
console.log("Pass?", match);
