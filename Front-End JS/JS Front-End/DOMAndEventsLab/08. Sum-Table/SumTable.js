function sumTable() {
    let tabel = document.getElementsByTagName("tbody")[0].children

    let result = 0

    for (let num = 1; num < tabel.length -1; num ++){
        result += Number(tabel[num].children[1].innerText)
        
    }

    document.getElementById("sum").innerText = result
}