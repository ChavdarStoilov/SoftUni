function radar(speed, area) {

    speedLimits = {
        "motorway": 130,
        "interstate": 90,
        "city": 50,
        "residential": 20
    }

    if (speed > speedLimits[area]) {
        let status;
        difference = speed - speedLimits[area]
        
        if (difference <= 20){
            status = "speeding"
        }
        else if (difference <= 40) {
            status = "excessive speeding"
        }
        else {
            status = "reckless driving"
        }
        
        return `The speed is ${speed - speedLimits[area]} km/h faster than the allowed speed of ${speedLimits[area]} - ${status}`
    }
    else {
        return `Driving ${speed} km/h in a ${speedLimits[area]} zone`
    }
}

console.log(radar(40, 'city'));
console.log(radar(21, 'residential'));
console.log(radar(120, 'interstate'));
console.log(radar(200, 'motorway'))