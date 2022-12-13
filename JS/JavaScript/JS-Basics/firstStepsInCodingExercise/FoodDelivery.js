function delivery(inputs) {

    let chicken = parseInt(inputs[0]);
    let fish = parseInt(inputs[1]);
    let veg = parseInt(inputs[2]);

    let priceForChicken = 10.35;
    let priceForFish = 12.40;
    let priceForVeg = 8.15;

    let priceForDelivery = 2.50;

    let sum = (chicken * priceForChicken) + (fish * priceForFish) + (veg * priceForVeg);

    let desert = sum * 0.20;

    let end_sum = sum + desert + priceForDelivery;

    console.log(end_sum);
}


delivery(["2 ",
"4 ",
"3 "]
);