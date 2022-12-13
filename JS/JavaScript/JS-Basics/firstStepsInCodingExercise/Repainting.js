function repair(inputs) {

    let neededNylon = parseInt(inputs[0]) + 2;
    let neededPaint = parseInt(inputs[1]) + parseInt(inputs[1]) * 0.10;
    let neededThinner = parseInt(inputs[2]);
    let hours = parseInt(inputs[3]);

    let bag = 0.40;

    let nylonPricePerMeter =  1.50;
    let paintPricePerLiter =  14.50;
    let thinnerPricePerLiter = 5.00;


    let sumForNylon =  neededNylon * nylonPricePerMeter;
    let sumForPaint = neededPaint * paintPricePerLiter;
    let sumForThinner = neededThinner * thinnerPricePerLiter;

    let sumForMaterials = sumForNylon + sumForPaint + sumForThinner + bag;

    let sumForWorkerPerHour = sumForMaterials * 0.30;

    let sumForWorker = sumForWorkerPerHour * hours;

    let endSum = sumForMaterials + sumForWorker;

    console.log(endSum);


}

repair(["10 ",
"11 ",
"4 ",
"8 "]
);