function promotions(day, age) {
    var price;

    if (day == "Weekday"){
        if (0 <= age && age <= 18) {
            price = 12    
        }
        else if (18 < age && age <= 64) {
            price = 18
        }
        else if (65 < age && age <= 122) {
            price = 12
        }
        else {
            return "Error!"
        }
    }
    else if (day == "Weekend") {
        if (0 <= age && age <= 18) {
            price = 15    
        }
        else if (18 < age && age <= 64) {
            price = 20
        }
        else if (65 < age && age <= 122) {
            price = 15
        }
        else {
            return "Error!"
        }
    }
    else if (day == "Holiday") {
        if (0 <= age && age <= 18) {
            price = 5    
        }
        else if (18 < age && age <= 64) {
            price = 12
        }
        else if (65 < age && age <= 122) {
            price = 10
        }
        else {
            return "Error!"
        }
    }
    else {
        return "Error!"
    }

    return `${price}$`
}

console.log(promotions('Holiday', 15));