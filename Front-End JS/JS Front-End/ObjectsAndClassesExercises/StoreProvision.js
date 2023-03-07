function sotre(stock, ordered) {
    
    let localStoreStock = {

    }

    for (let i = 0; i < stock.length; i+= 2){
        let [product, count] =stock.slice(i,i+2);

        localStoreStock[product] = Number(count)
    }

    for (let i = 0; i < ordered.length; i+= 2) {
        let [product, count] = ordered.slice(i,i+2);

        if (!(product in localStoreStock)) {
            localStoreStock[product] = Number(count)
        }
        else {
            localStoreStock[product] += Number(count)
        }
    }

    for (key in localStoreStock) {
        console.log(`${key} -> ${localStoreStock[key]}`);
    }
}


sotre([
    'Chips', '5', 'CocaCola', '9', 'Bananas',
    '14', 'Pasta', '4', 'Beer', '2'
    ],
    
    [
    'Flour', '44', 'Oil', '12', 'Pasta', '7',
    'Tomatoes', '70', 'Bananas', '30'
    ])