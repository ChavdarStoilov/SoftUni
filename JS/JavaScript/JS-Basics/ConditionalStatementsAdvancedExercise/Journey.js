function vacation(inputs) {
    
    let budget = parseFloat(inputs[0]);
    let session = String(inputs[1]);

    let destination;
    let amount;
    let typeVacation;

    if (budget <= 100) {
        destination = "Bulgaria";
        if (session == "summer") {
            amount = budget * 0.30;
            typeVacation = "Camp";
        }
        else if (session == "winter") {
            amount = budget * 0.70;
            typeVacation = "Hotel";
        };
    }   
    else if (budget <= 1000) {
        destination = "Balkans";
        if (session == "summer") {
            amount = budget * 0.40;
            typeVacation = "Camp";

        }
        else if (session == "winter") {
            amount = budget * 0.80;
            typeVacation = "Hotel";

        };
    }
    else if (budget > 1000) {
        destination = "Europe";
        amount = budget * 0.90
        typeVacation = "Hotel";
    };

    console.log(`Somewhere in ${destination}`)
    console.log(`${typeVacation} - ${amount.toFixed(2)}`)

}

vacation(["50", "summer"])
vacation(["75", "winter"])
vacation(["312", "summer"])
vacation(["678.53", "winter"])
vacation(["1500", "summer"])

