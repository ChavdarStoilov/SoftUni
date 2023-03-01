function solve() {
    let info = document.querySelector("#info span")
    let btnDepart = document.getElementById("depart")
    let btnArraival = document.getElementById("arrive")
    let ids = "depot"
    let currentStop = ""
    
    function depart() {
         // catching error and run function for present it
        let url = `http://localhost:3030/jsonstore/bus/schedule/${ids}`
        fetch (url)
            .then(response => response.json()) // convert response to json
            .then((data) =>{
                ids = data["next"]
                currentStop = data["name"]
                info.textContent = `Next stop ${data["name"]}`
                btnDepart.disabled = true;
                btnArraival.disabled = false;
            }) 
            .catch(() =>{
                info.textContent = "Error"
                btnDepart.disabled = true;
                btnArraival.disabled = true;
            })

    }

    async function arrive() {

        info.textContent = `Arriving at ${currentStop}`
        btnArraival.disabled = true;
        btnDepart.disabled = false;

    }
        

    return {
        depart,
        arrive
    };
}

let result = solve();