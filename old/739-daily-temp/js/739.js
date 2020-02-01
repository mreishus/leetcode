#!/usr/bin/env node

const dailyTemperatures = temps => {
    const answer = new Array(temps.length).fill(0);
    // Start from right of array and go left.
    // The right-most is already correct answer: 0, so start at length - 2.
    for (let i = temps.length - 2; i >= 0; i--) {
        // Skip to the right, looking for higher temperatures, but
        // use information we've already figured out.
        for (let j = i+1; j < temps.length; j += answer[j]) {
            if (temps[j] > temps[i]) {
                answer[i] = j - i;
                break;
            }
            if (answer[j] == 0) {
                break;
            }
        }
    }
    return answer;
};

let test = (expectedResult, actualResult) => {
    console.log("Expected result:", expectedResult);
    console.log("Actual result:", actualResult);
    match = JSON.stringify(actualResult) == JSON.stringify(expectedResult);
    console.log("Pass?", match);
};

let actualResult = dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]);
let expectedResult =            [1,   1,  4,  2,  1,  1,  0,  0];
test(expectedResult, actualResult);

actualResult = dailyTemperatures([55,38,53,81,61,93,97,32,43,78]);
expectedResult =                 [3, 1, 1, 2, 1, 1, 0, 1, 1,  0];
test(expectedResult, actualResult);
