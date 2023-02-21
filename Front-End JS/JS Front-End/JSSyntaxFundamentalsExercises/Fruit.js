function fruits(fruit, weight, pricePerKilogram) {

    return `I need $${((weight / 1000) * pricePerKilogram).toFixed(2)} to buy ${(weight / 1000).toFixed(2)} kilograms ${fruit}.`
}

console.log(fruits('apple', 1563, 2.35))