function house(inputs) {

    let type = String(inputs[0]);
    let count = Number(inputs[1]);
    let budget = Number(inputs[2]);

    let amount;

    if (type == "Roses") {
        amount = count * 5;

        if (count > 80) {
            amount -= amount * 0.10;
        };   
    }
    else if (type == "Dahlias") {
        amount = count * 3.80;

        if (count > 90) {
            amount -= amount * 0.15;
        };
    }
    else if (type == "Tulips") {
        amount = count * 2.80;

        if (count > 80) {
            amount -= amount * 0.15;
        };
    }
    else if (type == "Narcissus") {
        amount = count * 3;

        if (count < 120) {
            amount += amount * 0.15;
        };
    }
    else if (type == "Gladiolus") {
        amount = count * 2.50;

        if (count < 80) {
            amount += amount * 0.20;
        };

    };

    if (amount <= budget) {
        console.log(`Hey, you have a great garden with ${count} ${type} and ${(budget - amount).toFixed(2)} leva left.`);
    }
    else {
        console.log(`Not enough money, you need ${(amount - budget).toFixed(2)} leva more.`);
    };

}

house(["Roses","55","250"])
house(["Tulips","88","260"])
house(['Gladiolus', '64', '160'])