function checkNumber(someNumber){

    let number = Number(someNumber[0])

    if (number < 100){
        console.log("Less than 100")
    }
    
    else if (100 >= number) {
        console.log("Between 100 and 200")
    }

    else if (number <= 200) {
        console.log("Between 100 and 200")
    }

    else{
        console.log("Greater than 200")
    };
}


checkNumber(["95"])
checkNumber(["120"])
checkNumber(["210"])
