function passwordRecognizer(string) {

    let gavePassword = String(string[0])

    let correctPassword = "s3cr3t!P@ssw0rd"

    if (gavePassword == correctPassword) {
        console.log("Welcome")

    } 
    
    else {
        console.log("Wrong password!")
    };

}

passwordRecognizer(["qwerty"]);
passwordRecognizer(["s3cr3t!P@ssw0rd"]);
passwordRecognizer(["s3cr3t!p@ss"]);
