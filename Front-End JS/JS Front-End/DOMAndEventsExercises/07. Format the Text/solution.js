function solve() {
  document.getElementById("output").innerHTML = ""
  let input = document.getElementById("input").value.split(".");
  let output = document.getElementById("output");
  let p = ""

  if (input.length <= 3) {
    let newParg = document.createElement("p");
    newParg.textContent = input.join(".");
    output.appendChild(newParg);

  }
  else {

    for (var i = 1; i < input.length; i++ ){
      p += `${input[i-1]}.`
      if (i % 3 == 0) {
        // console.log(p);
        let newParg = document.createElement("p");
        newParg.textContent = p;
        output.appendChild(newParg);
        p = ""
      }
    
    }
    if (p) {
      let newParg = document.createElement("p");
      newParg.textContent = p;
      output.appendChild(newParg);
    }


  }

  document.getElementById("input").value = ""
}
