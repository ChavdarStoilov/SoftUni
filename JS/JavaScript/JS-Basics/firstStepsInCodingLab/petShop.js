function shop(data){
    let countDog = data[0]
    let countCat = data[1]
    let priceDog = 2.50
    let priceCat = 4

    let result = (countCat * priceCat) + (countDog * priceDog)

    console.log(`${result} lv.`);
}

shop(["13 ", "9"])