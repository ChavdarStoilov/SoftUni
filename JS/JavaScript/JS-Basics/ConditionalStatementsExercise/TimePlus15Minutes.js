function plus15(input) {
    
    let hours = Number(input[0]);
    let minutes = Number(input[1]);

    let countMinutes = hours * 60 + minutes + 15;

    if (Math.floor(countMinutes / 60) == 24){
        console.log(`0:${String(countMinutes % 60).padStart(2, "0")}`);

    }
    else {
        console.log(`${Math.floor(countMinutes / 60)}:${String(countMinutes % 60).padStart(2, "0")}`);

    }


}

plus15(["23", "59"])