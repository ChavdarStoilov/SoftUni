function boat(inputs) {

    let budget = Number(inputs[0]);
    let session = String(inputs[1]);
    let people = Number(inputs[2]);

    let amount;
    let discount;

    if (people <= 6) {
        discount = 0.10;
    }

    else if (people > 7 && people <= 11) {
        discount = 0.15;
    }

    else if (people > 12) {
        discount = 0.25;
    };

    if (session == "Spring") {
        let boat = 3000;

        amount  = boat - boat * discount;
    }
    else if (session == "Summer" ) {
        let boat = 4200;

        amount  = boat - boat * discount;
    }

    else if (session == "Autumn") {
        let boat = 4200;

        amount  = boat - boat * discount;
    }

    else if (session == "Winter") {
        let boat = 2600;

        amount  = boat - boat * discount;
    };

    if (people % 2 == 0 && session != "Autumn") {
        amount -= amount * 0.05
    }

    if (amount <= budget) {
        console.log(`Yes! You have ${(budget - amount).toFixed(2)} leva left.`);
    }

    else if (amount > budget) {
        console.log(`Not enough money! You need ${(amount - budget).toFixed(2)} leva.`)
    }
}

boat(["3000",
"Summer",
"11"])
