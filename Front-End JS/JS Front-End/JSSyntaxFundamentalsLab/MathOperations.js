function mathOperations(numberOne, numberTwo, operator) {
    var result = 0

    if (operator == "+") {
        result = numberOne + numberTwo;

    } else if (operator == "-") {
        result = numberOne - numberTwo;

    } else if (operator == "*") {
        result = numberOne * numberTwo;

    } else if (operator == "/") {
        result = numberOne / numberTwo;

    } else if (operator == "%") {
        result = numberOne % numberTwo;

    } else if (operator == "**") {
        result = numberOne ** numberTwo;

    };

    return result;
}


console.log(mathOperations(3, 5.5, '*'))