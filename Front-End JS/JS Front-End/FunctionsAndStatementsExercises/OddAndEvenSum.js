function oddEven(number) {
    let sumOdd = 0
    let sumEven = 0
    let numberString = String(number)

    for (let i = 0; i < numberString.length; i++) {
        numberNum = Number(numberString[i])

        if (numberNum % 2 == 0){
            sumEven += numberNum
        }
        else {
            sumOdd += numberNum
        }
    }

    return `Odd sum = ${sumOdd}, Even sum = ${sumEven}`
    
}

console.log(oddEven(1000435))