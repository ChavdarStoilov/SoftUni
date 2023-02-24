function perfectNumber(number) {

    let result = 0

    for (let num = 1; num <= number; num++) {

        let test = Math.floor(number / num)

        if (number * num == number) {
            result += num
        }
        else if (number == test * num) {
            result += num
        }

    }

    
    if (Math.floor(result / 2) == number) {
        return "We have a perfect number!"
    }
    else {
        return "It's not so perfect."
    }
    
}
// for number in range(1, the_number +1):
//         test = the_number // number
//         if the_number * number == the_number:
//             result += number
//         elif the_number == test * number:
//             result += number

//     if result // 2 == the_number:
//         return "We have a perfect number!"
//     else:
//         return "It's not so perfect."

console.log(perfectNumber(6))