function months_get(number) {
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",

    };

    if (number < 1 || number > 12) {
        return "Error!";
    }

    else {
        return months[number];
    }

}


console.log(months_get(13))
 	