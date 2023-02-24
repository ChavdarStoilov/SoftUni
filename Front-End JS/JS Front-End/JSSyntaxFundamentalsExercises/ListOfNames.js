function sorting(arr) {
    let number = 1
    sorted = arr.sort()
    for (i in sorted) {
        console.log(`${number}.${sorted[i]}`);
        number ++ 
    }
    
}

sorting(["John", "Bob", "Christina", "Ema"]);