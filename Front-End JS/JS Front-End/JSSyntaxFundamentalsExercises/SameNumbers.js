function SameNumbers(number) {

    let sum = 0;
    let bool = false;
    let oldNumber = String(number)[0];
    let counter = 0;

    for (i of String(number)){
        sum += Number(i)

        if (oldNumber != i) {
            oldNumber = i
        }
        else {
            counter +=1
        }
    }

    if (counter == String(number).length){
        bool = true
    }

    console.log(bool)
    console.log(sum)

    
}

SameNumbers(2222222)