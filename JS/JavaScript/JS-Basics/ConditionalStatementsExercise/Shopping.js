function shopping(inputs) {
    let budget = parseFloat(inputs[0]);
    let videos = Number(inputs[1]);
    let processors = Number(inputs[2]);
    let ram = Number(inputs[3]);

    let priceProcessor = videos * 250 * 0.35;
    let priceRam = videos * 250 * 0.10;

    let discount = 0;

    if (videos > processors) {
        discount = 0.15;
    }

    let price = videos * 250 + priceProcessor * processors + priceRam * ram;
    let endPrice = price - price * discount

    if (budget >= endPrice) {
        console.log(`You have ${(budget - endPrice).toFixed(2)} leva left!`);
    }
    else {
        console.log(`Not enough money! You need ${(endPrice - budget).toFixed(2)} leva more!`)
    }

}

shopping(["920.45",
"3",
"1",
"1"])
