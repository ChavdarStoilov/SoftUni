function printer(arrry, step) {
    let newArry = []

    for (let i = 0; i <= arrry.length; i += step){
        newArry.push(arrry[i])
    }

    return newArry
    
}

console.log(printer(['5', 
'20', 
'31', 
'4', 
'20'], 
2
));