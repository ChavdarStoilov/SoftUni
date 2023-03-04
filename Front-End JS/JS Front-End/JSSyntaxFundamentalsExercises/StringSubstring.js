function substring(parm, searching) {
    let re = new RegExp(parm, 'gi');
    let result = searching.match(re)
    if( result === null){
        return `${parm} not found!`;
    }
    else {
        return parm;
    };
}

console.log(
  substring("JavaScript", "JavaScript is JavaScript the best programming language")
);

console.log(substring("python", "JavaScript is the best programming language"));
