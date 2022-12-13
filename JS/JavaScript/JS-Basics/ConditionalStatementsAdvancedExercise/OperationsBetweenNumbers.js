function calculator(inputs) {

    let numberOne = Number(inputs[0])
    let numberTwo = Number(inputs[1])
    let operator = String(inputs[2])

    let result;
    let evenOrOdd;

    if (operator == "+") {
        sum = numberOne + numberTwo;
        if (sum % 2 == 0) {
            evenOrOdd = "even";
        }
        else {
            evenOrOdd = 'odd';
        }
        result = `${numberOne} ${operator} ${numberTwo} = ${sum} - ${evenOrOdd}`;
    }
    else if (operator == "-") {
        sum = numberOne - numberTwo;
        if (sum % 2 == 0) {
            evenOrOdd = "even";
        }
        else {
            evenOrOdd = 'odd';
        }
        result = `${numberOne} ${operator} ${numberTwo} = ${sum} - ${evenOrOdd}`;
    }
    else if (operator == "*") {
        sum = numberOne * numberTwo;
        if (sum % 2 == 0) {
            evenOrOdd = "even";
        }
        else {
            evenOrOdd = 'odd';
        }
        result = `${numberOne} ${operator} ${numberTwo} = ${sum} - ${evenOrOdd}`;
    }
    else if (operator == "/") {
        if (numberOne == 0 ) {
            result = `Cannot divide ${numberTwo} by zero`;
        }
        else if (numberTwo == 0) {
            result = `Cannot divide ${numberOne} by zero`;
        }
        else {
            sum = (numberOne / numberTwo).toFixed(2);
            result = `${numberOne} ${operator} ${numberTwo} = ${sum}`;
        };
    }
    else if (operator == "%") {
        if (numberOne == 0 ) {
            result = `Cannot divide ${numberTwo} by zero`;
        }
        else if (numberTwo == 0) {
            result = `Cannot divide ${numberOne} by zero`;
        }
        else {
            sum = numberOne % numberTwo;
            result = `${numberOne} ${operator} ${numberTwo} = ${sum}`;
        };
    };

    console.log(result);
}

calculator(["10","12","+"])
calculator(["123","12","/"])
calculator(["112","0","/"])
calculator(["10","0","/"])
calculator(["10","1","-"])


