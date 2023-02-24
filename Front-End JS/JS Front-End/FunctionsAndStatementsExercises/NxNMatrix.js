function matrix(size) {
    result = "";

    for (let i = 1; i <= size; i++) {
        
        for (let i = 1; i <= size; i ++){
            result += size + " "
        }
        result += "\n"

    };

    console.log(result);
    
}

matrix(3)