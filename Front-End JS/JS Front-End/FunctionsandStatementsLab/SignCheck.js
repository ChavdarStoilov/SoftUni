function sign(numOne, numTwo, numThree){

    if (numOne * numTwo * numThree < 0){
        return "Negative"
    }
    else {
        return "Positive"
    }
}

console.log(sign(-6,
    -12,
     14
    )
);
