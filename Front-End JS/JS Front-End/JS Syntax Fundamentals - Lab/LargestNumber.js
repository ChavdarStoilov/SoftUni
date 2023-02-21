function largestNumber(firstNumber, secondNumber, thirdNumber) {
    
    var maxNumber =  Math.max(firstNumber, secondNumber, thirdNumber);

    return `The largest number is ${maxNumber}.`;
};

console.log(largestNumber(-3, -5, -22.5));