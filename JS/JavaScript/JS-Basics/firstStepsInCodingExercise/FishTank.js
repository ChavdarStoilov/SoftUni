function aqu(inputs) {

    let length = parseInt(inputs[0]);
    let width = parseInt(inputs[1]);
    let hight = parseInt(inputs[2]);
    let percent = parseFloat(inputs[3]) / 100;

    let liters = (length * width * hight) * 0.001
    
    let neededLiters = liters * (1 - percent);

    console.log(neededLiters);

}

aqu(["85 ",
"75 ",
"47 ",
"17 "]
);