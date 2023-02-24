function reverse(number, array) {
    let newArray = [];

    for (let i = 0; i < number; i++) {
        newArray.push(array[i]);
    }

    return newArray.reverse().join(" ");
}

console.log(reverse(3, [10, 20, 30, 40, 50]));