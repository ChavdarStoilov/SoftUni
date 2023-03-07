function meetingScheduler(arry) {

    let meetings = {

    }

    for (row in arry) {
        let [day, name] = arry[row].split(" ")

        if (!(day in meetings)) {
            meetings[day] = name
            console.log(`Scheduled for ${day}`);
        }
        else {
            console.log(`Conflict on ${day}!`);
        }
        
    }

    for (days in meetings) {
        console.log(`${days} -> ${meetings[days]}`);
    }
    
}

meetingScheduler(['Friday Bob',
'Saturday Ted',
'Monday Bill',
'Monday John',
'Wednesday George'])