function modern(inpt){
    console.log(inpt.match(/(?<=[#])[a-zA-Z]+/g).join("\n"));
}

modern('Nowadays everyone uses # to tag a #special word in #socialMedia')
modern('The symbol # is known #variously in English-speaking #regions as the #number sign')
