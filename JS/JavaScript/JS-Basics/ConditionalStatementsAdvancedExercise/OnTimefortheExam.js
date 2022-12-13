function exam(inputs) {
    let examHourTime = Number(inputs[0]);
    let examMinuteTime = Number(inputs[1]);
    let appearHourTime = Number(inputs[2]);
    let appearMinuteTime = Number(inputs[3]);

    let startExamInMinutes = (examHourTime * 60) + examMinuteTime;
    let appearInMinutes = (appearHourTime * 60) + appearMinuteTime;

    let different =  appearInMinutes - startExamInMinutes;

    if (different < 0){
        let minutes = different * -  1;
        if (minutes <= 30 && minutes < 60) {
            console.log("On time");
            console.log(`${minutes} minutes before the start`);
        }
        else if (minutes > 30 && minutes >= 60) {
            console.log("Early");
            console.log(`${String((minutes / 60))[0]}:${String(minutes % 60).padStart(2, "0")} hours before the start`);
        }
        else{
            console.log("Early");
            console.log(`${minutes} minutes before the start`);
        };

    }

    else if (different > 0){
        console.log("Late");
        if (different < 60) {
            console.log(`${different} minutes after the start`);
        }
        else if (different >= 60) {
            console.log(`${String((different / 60))[0]}:${String(different % 60).padStart(2, "0")} hours after the start`);
        };
    }
    else {
        console.log("On time");
    }

}

exam(["11",
"30",
"8",
"12"])




















