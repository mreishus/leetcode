#!/usr/bin/env node

let countBits = num => {
    let result = [];
    for (let i = 0; i<= num; i++) {
        result.push(i);
    }
    return result.map(x => count_binary_ones(x));
};

let count_binary_ones = num => {
	let count = 0;
    while (num > 0) {
        if (num % 2 == 1) {
            count += 1;
        }
        num = num >> 1;
    }
    return count;
};


let actualResult = countBits(5);
let expectedResult = [0, 1, 1, 2, 1, 2];
console.log("Expected result:", expectedResult);
console.log("Actual result:", actualResult);
let match = JSON.stringify(actualResult) == JSON.stringify(expectedResult);
console.log("Pass?", match);
