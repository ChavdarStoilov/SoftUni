function parking(arry) {
    let park = []

    for (let i = 0; i < arry.length; i ++) {
        let [move, number] = arry[i].split(", ");

        if (move === "IN" && !(number in park)) {
            park.push(number)
        }
        else if (move === "OUT" && park.includes(number)){
            index = park.indexOf(number)
            park.splice(index, 1)
        }
    }


    if (park.length > 0){
        console.log(park.sort().join("\n"))
    }
    else {
        console.log("Parking Lot is Empty");
    };
}


parking(['IN, CA2844AA', 'IN, CA1234TA', 'OUT, CA2844AA', 'IN, CA9999TT', 'IN, CA2866HI', 'OUT, CA1234TA', 'IN, CA2844AA', 'OUT, CA2866HI', 'IN, CA9876HH', 'IN, CA2822UU'])