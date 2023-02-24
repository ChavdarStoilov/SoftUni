function loadingBar(percent) {
    theBar = [".",".",".",".",".",".",".",".",".","."]
    progress = percent / 10
    
    if (percent == 100){
        theBar = ["%","%","%","%","%","%","%","%","%","%"]
        console.log("100% Complete!");
        console.log(`[${theBar.join("")}]`)

    }
    else {
        for (let i = 0; i < progress; i++){
            theBar[i] = "%"
        }
        console.log(`${percent}% [${theBar.join("")}]`)
        console.log("Still loading...");

    }



}

loadingBar(30)