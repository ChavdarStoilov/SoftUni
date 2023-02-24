function create(words) {
   let main = document.getElementById("content")

   for (div in words) {
      let newDiv = document.createElement("div")
      newDiv.innerHTML = `<p style='display:none'>${words[div]}</p>`
      main.appendChild(newDiv)
   }

   
   window.onclick = e => {
      id = e.target;  // to get the element
   id.firstChild.style.display = "block";
   }
}