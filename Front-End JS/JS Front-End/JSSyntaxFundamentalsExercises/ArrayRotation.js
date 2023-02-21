function rotating(arr, countRotate) {

    for (let i = countRotate; i > 0; i--){
        arr.push(arr.shift())
    }

    return arr.join(" ")
}

console.log(rotating([51, 47, 32, 61, 21], 2))
console.log(rotating([32, 21, 61, 1], 4))
console.log(rotating([2, 4, 15, 31], 5))

