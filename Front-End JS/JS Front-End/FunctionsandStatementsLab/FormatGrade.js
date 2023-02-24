function grades(grade) {
    if (grade < 3) {
        return `Fail (${2})`
    }
    else if (3.00 <= grade && grade < 3.50 ){
        return `Poor (${grade.toFixed(2)})`
    }
    else if (3.50 <= grade && grade < 4.50 ){
        return `Good (${grade.toFixed(2)})`
    }
    else if (4.50 <= grade && grade < 5.50 ){
        return `Very good (${grade.toFixed(2)})`
    }
    else if (5.50 <= grade) {
        return `Excellent (${grade.toFixed(2)})`
    }
}

console.log(grades(2.99));