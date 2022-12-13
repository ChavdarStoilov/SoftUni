function swimming(inputs) {
    let recordSeconds = parseFloat(inputs[0]);
    let meters = parseFloat(inputs[1]);
    let timePerMeterInSeconds = parseFloat(inputs[2]);
    
    let neededSeconds = (meters * timePerMeterInSeconds) + (Math.floor(meters / 15) * 12.5);

    if (neededSeconds < recordSeconds) {
        console.log(`Yes, he succeeded! The new world record is ${neededSeconds.toFixed(2)} seconds.`);
    }
    else {
        console.log(`No, he failed! He was ${(neededSeconds - recordSeconds).toFixed(2)} seconds slower.`);
    }
}

swimming(["55555.67",
"3017",
"5.03"])

