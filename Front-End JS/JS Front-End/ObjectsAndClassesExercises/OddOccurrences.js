function occurrences(words) {
    let wordsArry = words.split(" ")

    let odd = {

    }

    for (i in wordsArry) {
        let word = wordsArry[i]

        if (!(word.toLowerCase() in odd)) {
            odd[word.toLowerCase()] = 0
        }
        odd[word.toLowerCase()] ++
        
    }

    let keys = Object.keys(odd);
    keys.sort(function(a, b) { return odd[b] - odd[a] });
    
    output = []
    for (let i = 0; i < keys.length; i++) {
        if (odd[keys[i]] % 2 !== 0) {
            output.push(keys[i]);
        }
    }

    console.log(output.join(" "));
}

occurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')