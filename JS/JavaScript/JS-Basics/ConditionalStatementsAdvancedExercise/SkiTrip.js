function skiTrip(inputs) {
    let days = Number(inputs[0] - 1);
    let room = String(inputs[1]);
    let rate = String(inputs[2]);

    let amount;

    if (room == "room for one person") {
        amount = days * 18.00;
    }

    else if (room == "apartment") {
        amount = days * 25.00;
        if (days < 10) {
            amount -= amount * 0.30;
        }
        else if (days >= 10 && days < 15) {
            amount -= amount * 0.35;
        }
        else if (days > 15) {
            amount -= amount * 0.50;
        };
    }
    else if (room == "president apartment") {
        amount = days * 35;
        if (days < 10) {
            amount -= amount * 0.10;
        }
        else if (days >= 10 && days < 15) {
            amount -= amount * 0.15;
        }
        else if (days > 15) {
            amount -= amount * 0.20;
        }

    };

    if (rate == "positive") {
        amount += amount * 0.25;
    }
    else {
        amount -= amount * 0.10
    };

    console.log(amount.toFixed(2))
}


skiTrip(["12",
"room for one person",
"positive"])


