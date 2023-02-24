function extractText() {
    
    let list = document.getElementById("items").innerText;

    textarea = document.getElementById("result");

    textarea.value = list;
    
}