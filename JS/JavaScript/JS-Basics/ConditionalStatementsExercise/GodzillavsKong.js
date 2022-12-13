function movie(inputs) {
    let budget = parseFloat(inputs[0]);
    let statist = Number(inputs[1]);
    let pricePerStatist = parseFloat(inputs[2]);

    let decor = budget * 0.10;
    let discount = 0;

    if (statist > 150) {
        discount = 0.10;
    }

    let sumWithoutDiscount = (statist * pricePerStatist);
    let sum = sumWithoutDiscount - sumWithoutDiscount * discount + decor;

    if (budget >= sum) {
        console.log(`Action!\nWingard starts filming with ${(budget - sum).toFixed(2)} leva left.`);
    }
    else {
        console.log(`Not enough money!\nWingard needs ${(sum - budget).toFixed(2)} leva more.`);
    }



}

movie(["9587.88",
"222",
"55.68"])
