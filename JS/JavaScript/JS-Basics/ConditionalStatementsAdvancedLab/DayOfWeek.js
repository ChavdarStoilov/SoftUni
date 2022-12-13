function days(input) {
    let number = Number(input[0]);

    switch(number) {
        case 1:
            console.log("Monday");
            break;
        case 2:
            console.log("Tuesday");
            break
        case 3:
            console.log("Wednesday");
            break;
        case 4:
            console.log("Thursday");
            break;
        case 5:
            console.log("Friday");
            break;
        case 6:
            console.log("Saturday");
            break;
        case 7:
            console.log("Sunday");
            break;
        default:
            console.log("Error");
            break;
    }

}


days(["1"])
days(["2"])
days(["3"])
days(["4"])
days(["5"])
days(["6"])
days(["7"])
days(["-1"])
