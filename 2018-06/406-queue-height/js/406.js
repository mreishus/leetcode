#!/usr/bin/env node

const reconstructQueue = people => {
    // Sort from tallest to shortest
    // Tiebreak: Lower "K" numbers first.
    people.sort( (a, b) => {
        const heightSort = b[0] - a[0];
        const kSort = a[1] - b[1];
        return heightSort == 0 ? kSort : heightSort;
    });

    let q = [people.shift()];
    // Scan the array and insert the person at the correct position
    for (let p = 0; p < people.length; p++) {
        let person = people[p];
        q.splice(person[1], 0, person);
    }
    return q;
};

let test = (expectedResult, actualResult) => {
    console.log("Expected result:", expectedResult);
    console.log("Actual result:", actualResult);
    match = JSON.stringify(actualResult) == JSON.stringify(expectedResult);
    console.log("Pass?", match);
};

const input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]];
let actualResult = reconstructQueue(input);
let expectedResult = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]];
test(expectedResult, actualResult);

