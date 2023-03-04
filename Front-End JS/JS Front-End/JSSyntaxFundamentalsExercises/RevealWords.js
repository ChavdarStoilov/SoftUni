function reveal(words, template){
    words = words.split(", ");
    let forReplace = template.match(/(?<=[ *])[*]+/g);
    template = template.split(" ")

    for (i in template){
        if(template[i].startsWith("*")){
            for (w in words){
                if (words[w].length === template[i].length){
                    template[i] = words[w]
                }
            }
        }
        
    }

    return template.join(" ");
   
}

console.log(reveal('great, learning',
'softuni is ***** place for ******** new programming languages'
))
console.log(reveal('great',
'softuni is ***** place for learning new programming languages'));