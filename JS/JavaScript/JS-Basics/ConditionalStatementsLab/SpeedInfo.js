function speed(input) {

    let providedSpeed = parseFloat(input[0])

    if (providedSpeed <= 10){
        console.log("slow")
    }
    else if (providedSpeed > 10 && providedSpeed <= 50) {
        console.log("average")
    }
    else if (providedSpeed > 50 && providedSpeed <= 150) {
        console.log("fast")
    }

    else if (providedSpeed > 150 && providedSpeed <= 1000) {
        console.log("ultra fast")
    }

    else if (providedSpeed > 1000) {
        console.log("extremely fast")
    };

}


speed(["8"])
speed(["49.5"])
speed(["126"])
