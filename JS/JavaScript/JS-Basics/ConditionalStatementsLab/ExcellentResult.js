function grace(someGrace) {

    let theGrace = parseFloat(someGrace[0]);

    if (theGrace >= 5.50) {
        console.log('Excellent!');
    };


}


grace(["6"]);

grace(["5"]);

grace(["5.50"]);