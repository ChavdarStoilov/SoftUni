function pascalCase(params) {

    console.log(params.search(/[[:upper:]][[:lower:]]+/gi));
    
}

pascalCase('SplitMeIfYouCanHaHaYouCantOrYouCan');
pascalCase('HoldTheDoor');
pascalCase('ThisIsSoAnnoyingToDo');
