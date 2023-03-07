function editElement(htmlElement, textInElement, replacerText) {

    let element = htmlElement
    let newElementText = element.textContent.replace(textInElement, replacerText)
    element.textContent = newElementText

   
}