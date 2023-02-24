function uppercase(lettnes) {

    
    let test = lettnes.replace(",", "").replace("!", "").replace("?", "").toUpperCase()

    console.log(test.replaceAll(" ", ", "));
    
}

uppercase('Hi, how are you?')