function addItem() {

    input = document.getElementById("newItemText").value

    ul = document.getElementById("items").innerHTML += `<li>${input}</li>`
    console.log(ul);
}