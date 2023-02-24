function sum(numbOne, numTwo, numThree) {
    let sumOfFirstSecond = (numbOne + numTwo) - numThree

    return sumOfFirstSecond
}

function subtract(numOne, numTwo, numThree) {
    return sum(numOne, numTwo) - numThree
}

console.log(sum(23,
    6,
    10));