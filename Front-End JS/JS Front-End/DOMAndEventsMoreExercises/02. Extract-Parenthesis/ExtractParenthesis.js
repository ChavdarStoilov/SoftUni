function extract(content) {
    let text = document.getElementById(content)

    let result = text.textContent.match(/(?<=[(])\w+/g).join("; ")
    text.textContent =result
}