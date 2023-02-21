function digitSum(number) {
    let result = 0;

    for (i of String(number)){
        result += Number(i)
    }

    return result
}


console.log(digitSum(245678));