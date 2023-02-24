function colorize() {
    let table = document.getElementsByTagName("table")[0]


    for (let row = 1; row < table.rows.length; row++){
        if (row % 2 != 0){
            table.rows[row].style.backgroundColor = "Teal";
        }
    }
}