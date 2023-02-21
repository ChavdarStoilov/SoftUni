function sorting(arry) {
    let newArry = []
    let i = 1;
    
    while (arry) {
        let number = 0;
        if (arry.length == 0) {
            break
        };
        
        if (i % 2 == 0){
            number = Math.max(...arry);
        }
        else if (i % 2 != 0){
            number = Math.min(...arry);
        }
       

        newArry.push(number)

        arry.splice(arry.indexOf(number), 1)
        i++;
    }
    return newArry
}

console.log(sorting([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))
