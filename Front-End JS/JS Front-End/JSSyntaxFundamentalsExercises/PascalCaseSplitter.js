function pascalCase(params) {
    
    let words = [];
    let word = "";

    for (let i = 0; i < params.length; i++) {
        let char = params[i];

        if(char === char.toUpperCase()){
            if (word){
                words.push(word);
            }
            word = char;
        }
        else if(char === char.toLowerCase()){
            word += char;
        }
    };
    if (word){
        words.push(word);
    }

    return words.join(", ");
}

// pascalCase('SplitMeIfYouCanHaHaYouCantOrYouCan');
pascalCase('HoldTheDoor');
// pascalCase('ThisIsSoAnnoyingToDo');
