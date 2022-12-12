function price(data){
    let priceWithoutDiscount = data[0] * 7.61
    let discount = priceWithoutDiscount * 0.18
    let priceWithDiscount = priceWithoutDiscount - discount

    console.log(`The final price is: ${priceWithDiscount} lv.`);
    console.log(`The discount is: ${discount} lv.`);
}

price(['550'])