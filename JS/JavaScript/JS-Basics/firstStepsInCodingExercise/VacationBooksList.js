function vacation(input) {

    let pages = parseInt(input[0]);
    let pages_per_hour = parseInt(input[1]);
    let deadline = parseInt(input[2]);

    let needed_hours = pages / pages_per_hour / deadline;

    console.log(needed_hours);

}

vacation(["212 ",
"20 ",
"2 "]
);