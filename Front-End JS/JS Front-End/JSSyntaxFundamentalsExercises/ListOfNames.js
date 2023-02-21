function sorting(arr) {

    for (i in arr.sort()) {
        console.log(`${Number(i) + 1}.${arr.sort()[i]}`)
    }
    
}

sorting(["John", "Bob", "Christina", "Ema"]);