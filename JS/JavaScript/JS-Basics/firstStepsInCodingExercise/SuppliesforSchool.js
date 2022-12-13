function calculator(inputs) {

    let pensPacks = inputs[0]
    let markersPacks = inputs[1]
    let literPreparation = inputs[2]
    let discount = inputs[3] / 100

    let pensPack= 5.80;
    let markersPack = 7.20;
    let preparationsPerLiter = 1.20;

    let sumPens = pensPacks * pensPack;
    let sumMarkers = markersPacks * markersPack;
    let sumLitersPrice = literPreparation * preparationsPerLiter;

    let sumWithoutDiscount = sumPens + sumMarkers + sumLitersPrice
    let sumWithDiscount = sumWithoutDiscount - (sumWithoutDiscount) * discount;

    console.log(sumWithDiscount);
}


calculator(["2 ",
"3 ",
"4 ",
"25 "]
);