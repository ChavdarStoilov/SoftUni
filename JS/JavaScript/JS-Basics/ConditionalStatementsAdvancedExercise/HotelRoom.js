function hotel(inputs) {

    let month = String(inputs[0]);
    let days = Number(inputs[1]);

    let amountForStudio;
    let amountForApartment;

    if (month == "May" || month == "October") {
        amountForStudio = days * 50;
        amountForApartment = days * 65;

        if (days > 7 && days <= 14) {
            amountForStudio -= amountForStudio * 0.05;
        }
        else if (days > 14){
            amountForStudio -= amountForStudio * 0.30;
        };

        if (days > 14) {
            amountForApartment -= amountForApartment * 0.10;
        };
    }
    else if (month == "June" || month == "September") {
        amountForStudio = days * 75.20;
        amountForApartment = days * 68.70;

        if (days > 14) {
            amountForStudio -= amountForStudio * 0.20;
        };

        if (days > 14) {
            amountForApartment -= amountForApartment * 0.10;
        };
    }
    else if (month == "August" || month == "July") {
        amountForStudio = days * 76 ;
        amountForApartment = days * 77;

        if (days > 14) {
            amountForApartment -= amountForApartment * 0.10;
        };

    }

    console.log(`Apartment: ${amountForApartment.toFixed(2)} lv.`)
    console.log(`Studio: ${amountForStudio.toFixed(2)} lv.`)

}


hotel(["May",
"15"])
hotel(["June",
"14"])
hotel(["August",
"20"])
