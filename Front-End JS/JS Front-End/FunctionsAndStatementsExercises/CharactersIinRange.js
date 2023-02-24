function range(startChar, finishChar) {
    let result = "";
    let start = startChar.charCodeAt(0)
    let finish = finishChar.charCodeAt(0)

    if ( start > finish){
        start = finishChar.charCodeAt(0)
        finish = startChar.charCodeAt(0)
    };

    for (let i = start + 1; i < finish ; i++){
        result += `${String.fromCharCode(i)} `
    };

    return result;

}

console.log(range("C",
    "#"));