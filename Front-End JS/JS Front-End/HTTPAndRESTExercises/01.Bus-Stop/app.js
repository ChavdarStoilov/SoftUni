function getInfo() {
    
    let stopID = document.getElementById("stopId");
    let busName = document.getElementById("stopName");
    let busUl  = document.getElementById("buses");

    let busID = stopID.value
    
    busUl.innerHTML = ""
    stopID.value = ""

    let url = `http://localhost:3030/jsonstore/bus/businfo/${busID}`
    fetch (url)
    .then(response => response.json())
    .then(data => present(data))
    .catch(error)


    function present(data){
        if (data) {
            busName.textContent = data["name"]
            let buses = data["buses"]

            for (let i in buses){
                let li = document.createElement("li")
                li.textContent = `Bus ${i} arrives in ${buses[i]} minutes`
                busUl.appendChild(li)
            }
        }

    }

    function error(){
        busName.textContent = "Error"
    }

    
}