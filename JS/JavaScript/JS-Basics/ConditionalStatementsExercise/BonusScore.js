function bonus(inputs) {
    let number = Number(inputs[0]);

    let points = 0;

    if (number <= 100) {
        points = 5;
    }
    else if (number > 100 && number <= 1000) {
        points = number * 0.20;
    }
    else if (number > 1000) {
        points = number * 0.10;
    };

    if (number % 2 == 0) {
        points += 1;
    };

    if (String(number).slice(-1) == 5) {
        points += 2;
    };
    
    console.log(points);
    console.log(number + points)

}

bonus(["15875"])