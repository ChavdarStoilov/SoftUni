
function addItem() {
    let newItem = document.getElementById("newItemText").value 
    let list  = document.getElementById("items")

    let li = document.createElement("li");
    li.appendChild(document.createTextNode(newItem));
    li.setAttribute("id", `${newItem}`);
    list.appendChild(li);
    
    document.getElementById(`${newItem}`).innerHTML += '<a href="#">[Delete]</a>'

    window.onclick = e => {
        id = e.target.parentNode.id;  // to get the element

        if (id) {
            document.getElementById(id).remove()
        }
    } 


}

