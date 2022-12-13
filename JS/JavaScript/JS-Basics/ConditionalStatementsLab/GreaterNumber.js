function greaterNumber(inputs) {

    let firstNumber = parseInt(inputs[0])
    let secondNumber = parseInt(inputs[1])

    if (firstNumber > secondNumber) {
        console.log(firstNumber)
    }
    else {
        console.log(secondNumber)
    };
}

greaterNumber(["5", "3"])