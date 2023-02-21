function calculateVacation(countPeople, type, day){
    let table = {
        "Students": {
            "Friday": 8.45,
            "Saturday": 9.80,
            "Sunday": 10.46,
        },
        "Business": {
            "Friday": 10.90,
            "Saturday": 15.60,
            "Sunday": 16,
        },
        "Regular": {
            "Friday": 15,
            "Saturday": 20,
            "Sunday": 22.50,
        }
    }

    let priceWithOutDiscount = countPeople * (table[type][day])

    if (30 <= countPeople && type === "Students"){
        priceWithOutDiscount -= priceWithOutDiscount * 0.15
    }
    else if (100 <= countPeople && type === "Business"){
        priceWithOutDiscount -= 10 * table[type][day]
    }
    else if (10 <= countPeople && countPeople <= 20 && type === "Regular"){
        priceWithOutDiscount -= priceWithOutDiscount * 0.05
    }

    return `Total price: ${priceWithOutDiscount.toFixed(2)}`

}

console.log(calculateVacation(11,
    "Regular",
    "Saturday"
    ));