function sumOrder(product, ordered) {
    prices = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00

    }

    return (prices[product] * ordered).toFixed(2)
    
}

console.log(sumOrder("water", 5));
console.log(sumOrder("coffee", 2));