function subtraction(array) {
    let evenResult = 0;
    let oddResult = 0;

    for (let x in array) {
        if (array[x] % 2 == 0){
            evenResult += array[x];
        }
        else {
            oddResult += array[x];
        }
    }

    return evenResult - oddResult;
}

console.log(subtraction([1,2,3,4,5,6]));