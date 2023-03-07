function trecker(arry) {
    let words = arry[0].split(" ")
    
    counter = {

    }
    
    for (i in words) {
        counter[words[i]] = 0
    }
    

    for (let i = 1; i < arry.length; i ++) {
        if (arry[i] in counter){
            counter[arry[i]] ++
        }
    }


    let keys = Object.keys(counter);
    keys.sort(function(a, b) { return counter[b] - counter[a] });

    for (let i in keys){
        console.log(`${keys[i]} - ${counter[keys[i]]}`)
    }
}



trecker([

    'this sentence',
    
    'In', 'this', 'sentence', 'you', 'have',
    
    'to', 'count', 'the', 'occurrences', 'of',
    
    'the', 'words', 'this', 'and', 'sentence',
    
    'because', 'this', 'is', 'your', 'task'
    
])