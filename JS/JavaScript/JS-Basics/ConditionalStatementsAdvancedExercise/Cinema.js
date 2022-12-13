function cinema(inputs) {

    let typeTicket = String(inputs[0])
    let liens = Number(inputs[1])
    let columns = Number(inputs[2])

    let premierePrice = 12.00
    let normalPrice = 7.50
    let discount = 5.00

    let hall = liens * columns

    if (typeTicket == 'Premiere') {
        console.log((hall * premierePrice).toFixed(2) + " leva");
    }

    else if (typeTicket == 'Normal'){
        console.log((hall * normalPrice).toFixed(2) + " leva");
    }

    else if (typeTicket == 'Discount'){
         console.log((hall * discount).toFixed(2) + " leva");
    };

}

cinema(["Premiere","10","12"]);

cinema(["Normal","21","13"]);

cinema(["Discount","12","30"]);

