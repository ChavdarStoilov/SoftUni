function deleteByEmail() {
    
    let table = document.getElementById("customers").children[1].children
    let input = document.getElementsByName("email")[0].value
    let founded = false
    let forDelete = ""


    for (let i = 0; i < table.length; i++){
        if (table[i].cells[1].textContent == input){
            founded = true
            forDelete = table[i]
            break
        }
    }
    
    if (founded) {
        forDelete.outerHTML = ""
        document.getElementById("result").innerHTML = "Deleted."
    }
    else {
        document.getElementById("result").innerHTML = "Not found."

    }
    
}