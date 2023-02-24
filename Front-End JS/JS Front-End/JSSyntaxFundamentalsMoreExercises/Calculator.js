function calculator(numberOne, operator, numberTwo) {

    switch (operator) {
        case "+":
            console.log((numberOne + numberTwo).toFixed(2)); 
            break;
        case "-":
            console.log((numberOne - numberTwo).toFixed(2)); 
            break;
        case "/":
            console.log((numberOne / numberTwo).toFixed(2)); 
            break
        case "*":
            console.log((numberOne * numberTwo).toFixed(2)); 
            break;
    
    }

    
}

calculator(25.5,
    '-',
    3
    )