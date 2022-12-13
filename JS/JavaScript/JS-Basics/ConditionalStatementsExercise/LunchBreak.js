function lunch(inputs) {
    let serial = String(inputs[0]);
    let time = Number(inputs[1]);
    let brake = Number(inputs[2])

    let leftTime = brake - brake / 8 - brake / 4;

    if (leftTime >= time) {
        console.log(`You have enough time to watch ${serial} and left with ${Math.ceil(leftTime - time)} minutes free time.`);
    }
    else {
        console.log(`You don't have enough time to watch ${serial}, you need ${Math.ceil(time - leftTime)} more minutes.`);
    }
}

lunch(["Teen Wolf",
"48",
"60"])

