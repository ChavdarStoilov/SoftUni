function circleArea(input) {

    if (typeof(input) != "number") {
        return `We can not calculate the circle area, because we receive a ${typeof(input)}.`;
    }
    else {
        return (Math.PI * input * input).toFixed(2);
    }
    
}

console.log(circleArea(5));