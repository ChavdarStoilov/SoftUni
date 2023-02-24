function toggle() {
    let button = document.getElementsByTagName("span")[0]
 

    if (button.textContent == "Less") {
        document.getElementById("extra").style.display = "none"
        button.textContent = "More"

    }
    else if (button.textContent == "More") {
        document.getElementById("extra").style.display = "block"
        button.textContent = "Less"

    }

}