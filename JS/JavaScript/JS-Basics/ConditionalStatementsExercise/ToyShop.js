function shop(inputs) {
    let priceVacation = parseFloat(inputs[0]);
    let pizzle = Number(inputs[1]);
    let girls = Number(inputs[2]);
    let bears = Number(inputs[3]);
    let minions = Number(inputs[4]);
    let trucks = Number(inputs[5]);

    let sum = (pizzle * 2.60) + (girls * 3) + (bears * 4.10) + (minions * 8.20) + (trucks * 2);

    let countToys = pizzle + girls + bears + minions + trucks;

    if (countToys >= 50) {
        sum -= sum * 0.25;
    };

    let endSum = sum - sum * 0.10;

    if (endSum >= priceVacation) {
        console.log(`Yes! ${(endSum - priceVacation).toFixed(2)} lv left.`)
    }
    else {
        console.log(`Not enough money! ${(priceVacation - endSum).toFixed(2)} lv needed.`)
    };
}

shop(["320",
"8",
"2",
"5",
"5",
"1"])
