function area(inputs) {

    let figure = String(inputs[0])

    if (figure == 'square') {
        let length = parseFloat(inputs[1])

        console.log((length ** 2).toFixed(3))
    }
    
    else if (figure == 'rectangle') {
        let length = parseFloat(inputs[1])
        let side = parseFloat(inputs[2])
        console.log((length * side).toFixed(3))
    }
    else if (figure == 'circle') {
        let radius = parseFloat(inputs[1])
        console.log((Math.PI * (radius ** 2)).toFixed(3))
    }
    else if (figure == 'triangle'){
        let length = parseFloat(inputs[1])
        let length_two = parseFloat(inputs[2])
        console.log((length * length_two / 2).toFixed(3))
    }
    ;

    
}


area(["square", "5"])
area((["rectangle","7","2.5"]))
area((["circle","6"]))
area((["triangle","4.5","20"]))