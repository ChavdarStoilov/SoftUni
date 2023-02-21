function ages(age){

    let output;

    if (0 <= age && age <= 2){
        output = "baby";
    }
    else if (3 <= age && age <= 13) {
        output = "child";
    }
    else if (14 <= age && age <= 19) {
        output = "teenager";
    }
    else if (20 <= age && age <=65) {
        output = "adult";
    }
    else if (66 <= age){
        output = "elder";
    }
    else {
        output = "out of bounds";
    }

    return output;
    
}

console.log(ages(100));