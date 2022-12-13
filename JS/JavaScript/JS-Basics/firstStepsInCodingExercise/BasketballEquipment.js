function basketball(inputs) {

    let yearTax = parseInt(inputs[0]);

    let shoes = yearTax - yearTax * 0.40;
    let outfit = shoes - shoes * 0.20;
    let ball = outfit / 4;
    let accessory = ball / 5;

    let sum = shoes + outfit + ball  + accessory + yearTax;

    console.log(sum);

}

basketball(["365 "])