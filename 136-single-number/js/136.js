#!/usr/bin/env node

let singleNumber = nums => nums.reduce( (acc, x) => acc ^ x, 0 );

let actualResult = singleNumber([4,1,2,1,2]);
let expectedResult = 4;
console.log("Expected result:", expectedResult);
console.log("Actual result:", actualResult);
let match = JSON.stringify(actualResult) == JSON.stringify(expectedResult);
console.log("Pass?", match);
